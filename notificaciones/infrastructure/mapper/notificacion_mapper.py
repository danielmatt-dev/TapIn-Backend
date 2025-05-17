from abc import ABC, abstractmethod
from notificaciones.domain.dtos import NotificacionDTO
from notificaciones.infrastructure.notificacion_model import NotificacionModel

class NotificacionMapper(ABC):
    @abstractmethod
    def to_dto(self, model: NotificacionModel) -> NotificacionDTO:
        pass
