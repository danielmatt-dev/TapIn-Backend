import requests
from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.models import Application, AccessToken
from oauth2_provider.settings import oauth2_settings
from oauthlib.common import generate_token
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
import datetime

from personal.application.use_cases.use_cases import (
    RegistrarPersonal, EliminarPersonal,
    ConsultarEstadoPersonal, ActualizarPersonal, BuscarPersonalPorCorreo
)
from personal.domain.dtos import PersonalDTO
from personal.infrastructure.serializers import PersonalSerializer


@api_view(['POST'])
def buscar_por_correo(request, buscar_por_correo: BuscarPersonalPorCorreo):
    id_token = request.data.get('id_token')
    if not id_token:
        return Response({'error': 'Falta el id_token'}, status=status.HTTP_400_BAD_REQUEST)

    # 1. Verificar token con Google
    google_resp = requests.get(f'https://oauth2.googleapis.com/tokeninfo?id_token={id_token}')
    if google_resp.status_code != 200:
        return Response({'error': 'id_token inválido'}, status=status.HTTP_400_BAD_REQUEST)

    data = google_resp.json()
    email = data.get('email')
    aud = data.get('aud')

    client_id = '136929181439-7ile1qcatksnrhdplketasl265oun097.apps.googleusercontent.com'
    if aud != client_id:
        return Response({'error': 'audiencia inválida'}, status=status.HTTP_403_FORBIDDEN)

    # 2. Buscar en tabla Personal
    personal = buscar_por_correo.execute(email)
    if personal is None:
        return Response({'error': 'Usuario no autorizado'}, status=status.HTTP_403_FORBIDDEN)

    # 3. Obtener o crear usuario Django
    user, _ = User.objects.get_or_create(email=email, defaults={'username': email})

    # 4. Generar token OAuth2
    try:
        app = Application.objects.get(name='TapIn OAuth2')
    except Application.DoesNotExist:
        return Response({'error': 'App OAuth no encontrada'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    token_str = generate_token()
    expires = timezone.now() + datetime.timedelta(seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS)

    token = AccessToken(
        user=user,
        token=token_str,
        application=app,
        expires=expires,
        scope='read write',
    )
    token.save()

    # 5. Respuesta con rol y expiración
    return Response({
        'access_token': token.token,
        'token_type': 'Bearer',
        'expires_in': oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS,
        'rol': str(personal.rol),
    })

@csrf_exempt
@api_view(['POST'])
def registrar_personal_view(request, registrar_personal: RegistrarPersonal):
    ser = PersonalSerializer(data=request.data)
    if not ser.is_valid():
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    dto = PersonalDTO(
        id_personal = ser.validated_data.get('id_personal'),
        nombre      = ser.validated_data['nombre'],
        rol         = ser.validated_data['rol'],
        departamento= ser.validated_data['departamento'],
        correo      = ser.validated_data['correo'],
        estado      = ser.validated_data.get('estado','Habilitado')
    )
    creado = registrar_personal.execute(dto)
    return Response(PersonalSerializer(creado).data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def eliminar_personal_view(request, eliminar_personal: EliminarPersonal):
    idp = request.data.get('id_personal')
    if not idp:
        return Response({"error":"id_personal es requerido"},
                        status=status.HTTP_400_BAD_REQUEST)
    success = eliminar_personal.execute(idp)
    return Response({"success": success}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def consultar_estado_personal_view(request, consultar_estado_personal: ConsultarEstadoPersonal):
    lista = consultar_estado_personal.execute()
    return Response(PersonalSerializer(lista, many=True).data,
                    status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['POST'])
def actualizar_personal_view(request, actualizar_personal: ActualizarPersonal):
    ser = PersonalSerializer(data=request.data)
    if not ser.is_valid():
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    dto = PersonalDTO(
        id_personal = ser.validated_data['id_personal'],
        nombre      = ser.validated_data['nombre'],
        rol         = ser.validated_data['rol'],
        departamento= ser.validated_data['departamento'],
        correo      = ser.validated_data['correo'],
        estado      = ser.validated_data['estado']
    )
    upd = actualizar_personal.execute(dto)
    return Response(PersonalSerializer(upd).data, status=status.HTTP_200_OK)
