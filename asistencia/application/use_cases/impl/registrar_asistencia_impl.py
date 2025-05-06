from injector import inject
from asistencia.application.use_cases.use_cases import RegistrarAsistencia
from asistencia.domain.dtos import AsistenciaDTO
from asistencia.domain.asistencia import Asistencia
from asistencia.domain.ports import AsistenciaRepository
from asistencia.infrastructure.mapper.asistencia_mapper import AsistenciaMapper

class RegistrarAsistenciaImpl(RegistrarAsistencia):

    @inject
    def __init__(self,
                repository: AsistenciaRepository,
                mapper: AsistenciaMapper):
        
        self._repo   = repository
        self._mapper = mapper

    def execute(self, dto: AsistenciaDTO) -> AsistenciaDTO:
        
        entidad = Asistencia(
            id_registro_asistencia=0,
            id_alumno=dto.id_alumno,
            fecha=dto.fecha,
            hora=dto.hora,
            tipo_registro=dto.tipo_registro,
            tipo_acceso=dto.tipo_acceso,
            estado=dto.estado,
        )
        creado = self._repo.registrar(entidad)
        return self._mapper.to_dto(creado)
