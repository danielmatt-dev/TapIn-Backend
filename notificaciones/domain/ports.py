from abc import ABC, abstractmethod
from typing import Optional
from notificaciones.domain.dtos import NotificacionDTO

class NotificacionesRepository(ABC):
    @abstractmethod
    def get_by_id(self, id_notificacion: int) -> Optional[NotificacionDTO]:
        pass

class SMSGateway(ABC):
    @abstractmethod
    def send_sms(self, telefono: str, mensaje: str) -> bool:
        pass
