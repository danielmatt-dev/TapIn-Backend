from injector import inject
from typing import List
from asistencia.application.use_cases.use_cases import BuscarAsistencias
from asistencia.domain.dtos import AsistenciaDTO
from asistencia.domain.ports import AsistenciaRepository
from asistencia.infrastructure.mapper.asistencia_mapper import AsistenciaMapper

class BuscarAsistenciasImpl(BuscarAsistencias):

    @inject
    def __init__(self,
                repository: AsistenciaRepository,
                mapper: AsistenciaMapper):
        
        self._repo   = repository
        self._mapper = mapper

    def execute(self, id_alumno: str) -> List[AsistenciaDTO]:
        regs = self._repo.buscar_por_alumno(id_alumno)
        return [ self._mapper.to_dto(r) for r in regs ]
