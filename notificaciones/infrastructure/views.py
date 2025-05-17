from rest_framework.response import Response
from rest_framework import status
from notificaciones.domain.exceptions import NotificacionException

def handle_enviar_notificacion(request, use_case, nfc_dto, id_notificacion: int):

    try:
        success = use_case.execute(nfc_dto, id_notificacion)
        return Response({'success': success}, status=status.HTTP_200_OK)
    except NotificacionException as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response({'error': 'Error interno'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def handle_enviar_alerta(request, use_case, alumno_dto, id_notificacion: int):

    try:
        success = use_case.execute(alumno_dto, id_notificacion)
        return Response({'success': success}, status=status.HTTP_200_OK)
    except NotificacionException as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception:
        return Response({'error': 'Error interno'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
