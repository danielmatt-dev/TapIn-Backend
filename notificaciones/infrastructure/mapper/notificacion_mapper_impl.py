from notificaciones.infrastructure.mapper.notificacion_mapper import NotificacionMapper
from notificaciones.domain.dtos import NotificacionDTO
from notificaciones.infrastructure.notificacion_model import NotificacionModel

class NotificacionMapperImpl(NotificacionMapper):
    def to_dto(self, model: NotificacionModel) -> NotificacionDTO:
        return NotificacionDTO(
            id_notificacion = model.id_notificacion,
            titulo          = model.titulo,
            descripcion     = model.descripcion,
            tipo            = model.tipo,
            estado          = model.estado
        )
