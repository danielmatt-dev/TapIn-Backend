from injector import Injector
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from notificaciones.infrastructure.serializers import (
    NotificacionRequestSerializer,
    AlertaRequestSerializer
)
from notificaciones.infrastructure.views import (
    handle_enviar_notificacion,
    handle_enviar_alerta
)
from notificaciones.application.use_cases.use_cases import (
    EnviarNotificacion,
    EnviarAlerta
)
from notificaciones.infrastructure.injector_modules import NotificacionesInjectorModule
from nfc.domain.ports import NFCRepository
from alumnos.domain.ports import AlumnoRepository

@csrf_exempt
@api_view(['POST'])
def enviar_notificacion_view_factory(request):
    ser = NotificacionRequestSerializer(data=request.data)
    if not ser.is_valid():
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    inj        = Injector([NotificacionesInjectorModule])
    nfc_repo   = inj.get(NFCRepository)
    use_case   = inj.get(EnviarNotificacion)

    id_nfc          = ser.validated_data['id_nfc']
    id_notificacion = ser.validated_data['id_notificacion']
    nfc_dto         = nfc_repo.get_by_id(id_nfc)

    return handle_enviar_notificacion(request, use_case, nfc_dto, id_notificacion)

@csrf_exempt
@api_view(['POST'])
def enviar_alerta_view_factory(request):
    ser = AlertaRequestSerializer(data=request.data)
    if not ser.is_valid():
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    inj         = Injector([NotificacionesInjectorModule])
    alumno_repo = inj.get(AlumnoRepository)
    use_case    = inj.get(EnviarAlerta)

    id_alumno        = ser.validated_data['id_alumno']
    id_notificacion  = ser.validated_data['id_notificacion']
    alumno_dto       = alumno_repo.get_by_id(id_alumno)

    return handle_enviar_alerta(request, use_case, alumno_dto, id_notificacion)
