from typing import Optional
from notificaciones.domain.ports import NotificacionesRepository
from notificaciones.domain.dtos import NotificacionDTO
from notificaciones.infrastructure.notificacion_model import NotificacionModel
from notificaciones.infrastructure.mapper.notificacion_mapper import NotificacionMapper

class NotificacionesRepositoryImpl(NotificacionesRepository):
    def __init__(self, mapper: NotificacionMapper):
        self._mapper = mapper

    def get_by_id(self, id_notificacion: int) -> Optional[NotificacionDTO]:
        m = NotificacionModel.objects.filter(id_notificacion=id_notificacion).first()
        return self._mapper.to_dto(m) if m else None
