from injector import inject
from datetime import date
from typing import List
from asistencia.application.use_cases.use_cases import ConsultarAsistenciasDelDia
from asistencia.domain.dtos import AsistenciaDTO
from asistencia.domain.ports import AsistenciaRepository
from asistencia.infrastructure.mapper.asistencia_mapper import AsistenciaMapper

class ConsultarAsistenciasDelDiaImpl(ConsultarAsistenciasDelDia):

    @inject
    def __init__(self,
                repository: AsistenciaRepository,
                mapper: AsistenciaMapper):
        
        self._repo   = repository
        self._mapper = mapper

    def execute(self, fecha: date) -> List[AsistenciaDTO]:
        regs = self._repo.consultar_por_dia(fecha)
        return [ self._mapper.to_dto(r) for r in regs ]
