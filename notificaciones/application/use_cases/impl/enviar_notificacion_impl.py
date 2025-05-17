from injector import inject
from nfc.domain.ports import NFCRepository
from notificaciones.domain.ports import NotificacionesRepository, SMSGateway
from notificaciones.application.use_cases.use_cases import EnviarNotificacion
from notificaciones.domain.exceptions import (
    NotificacionNotFound, InvalidNotificacionType,
    DisabledNotificacion, PhoneNotFound
)

class EnviarNotificacionImpl(EnviarNotificacion):
    @inject
    def __init__(
        self,
        nfc_repo: NFCRepository,
        noti_repo: NotificacionesRepository,
        sms_gateway: SMSGateway,
    ):
        self._nfc_repo = nfc_repo
        self._noti_repo = noti_repo
        self._sms = sms_gateway

    def execute(self, id_nfc: int, id_notificacion: int) -> bool:
        # Obtiene datos de NFC (contiene alumno y su teléfono)
        dto_nfc = self._nfc_repo.get_by_id(id_nfc)
        if not dto_nfc:
            raise NotificacionNotFound(f"NFC {id_nfc} no encontrado")
        telefono = getattr(dto_nfc.alumno, "telefono_tutor", None)
        if not telefono:
            raise PhoneNotFound("Teléfono del tutor no disponible")

        # Obtiene plantilla de notificación
        plant = self._noti_repo.get_by_id(id_notificacion)
        if not plant:
            raise NotificacionNotFound(f"Notificación {id_notificacion} no encontrada")
        if plant.tipo != "Notificación":
            raise InvalidNotificacionType(f"ID {id_notificacion} no es de tipo Notificación")
        if plant.estado != "Habilitado":
            raise DisabledNotificacion(f"Notificación {id_notificacion} deshabilitada")

        # Formatea y envía SMS
        mensaje = plant.descripcion.format(nombre_alumno=dto_nfc.alumno.nombre_completo)
        return self._sms.send_sms(telefono, mensaje)
