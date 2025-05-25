from asistencia.domain.asistencia import Asistencia
from asistencia.domain.dtos import AsistenciaDTO
from asistencia.infrastructure.asistencia_model import AsistenciaModel
from asistencia.infrastructure.mapper.asistencia_mapper import AsistenciaMapper

class AsistenciaMapperImpl(AsistenciaMapper):

    def to_domain(self, model: AsistenciaModel) -> Asistencia:
        return Asistencia(
            id_registro_asistencia=model.id_registro_asistencia,
            id_alumno=model.id_alumno,
            fecha=model.fecha,
            hora=model.hora,
            tipo_registro=model.tipo_registro,
            tipo_acceso=model.tipo_acceso,
            estado=model.estado
        )

    def to_model(self, domain: Asistencia) -> AsistenciaModel:
        m = AsistenciaModel(
            id_alumno     = domain.id_alumno,
            fecha         = domain.fecha,
            hora          = domain.hora,
            tipo_registro = domain.tipo_registro,
            tipo_acceso   = domain.tipo_acceso,
            estado        = domain.estado,
        )
        if getattr(domain, 'id_registro_asistencia', None):
            m.id_registro_asistencia = domain.id_registro_asistencia
        return m

    def to_dto(self, domain: Asistencia) -> AsistenciaDTO:
        return AsistenciaDTO(
            id_registro_asistencia=domain.id_registro_asistencia,
            id_nfc=domain.id_alumno,
            fecha=domain.fecha,
            hora=domain.hora,
            tipo_registro=domain.tipo_registro,
            tipo_acceso=domain.tipo_acceso,
            estado=domain.estado
        )
