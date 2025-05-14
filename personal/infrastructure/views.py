from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from personal.application.use_cases.use_cases import (
    RegistrarPersonal, EliminarPersonal,
    ConsultarEstadoPersonal, ActualizarPersonal
)
from personal.domain.dtos import PersonalDTO
from personal.infrastructure.serializers import PersonalSerializer

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
