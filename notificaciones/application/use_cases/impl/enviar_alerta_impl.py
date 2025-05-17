from injector import inject
from alumnos.domain.dtos import AlumnoDTO
from notificaciones.domain.ports import NotificacionesRepository, SMSGateway
from notificaciones.application.use_cases.use_cases import EnviarAlerta
from notificaciones.domain.exceptions import (
    NotificacionNotFound, InvalidNotificacionType,
    DisabledNotificacion, PhoneNotFound
)

class EnviarAlertaImpl(EnviarAlerta):
    @inject
    def __init__(
        self,
        noti_repo: NotificacionesRepository,
        sms_gateway: SMSGateway,
    ):
        self._noti_repo = noti_repo
        self._sms = sms_gateway

    def execute(self, alumno: AlumnoDTO, id_notificacion: int) -> bool:
        telefono = alumno.telefono_tutor
        if not telefono:
            raise PhoneNotFound("Teléfono del tutor no disponible")

        plantilla = self._noti_repo.get_by_id(id_notificacion)
        if not plantilla:
            raise NotificacionNotFound(f"Alerta {id_notificacion} no encontrada")
        if plantilla.tipo != "Alerta":
            raise InvalidNotificacionType(f"ID {id_notificacion} no es de tipo Alerta")
        if plantilla.estado != "Habilitado":
            raise DisabledNotificacion(f"Alerta {id_notificacion} deshabilitada")

        mensaje = plantilla.descripcion.format(nombre_alumno=alumno.nombre_completo)
        return self._sms.send_sms(telefono, mensaje)
