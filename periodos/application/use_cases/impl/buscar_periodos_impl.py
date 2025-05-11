from injector import inject
from typing import List
from periodos.application.use_cases.use_cases import BuscarPeriodos
from periodos.domain.dtos import PeriodoDTO
from periodos.domain.ports import PeriodoRepository
from periodos.infrastructure.mapper.periodo_mapper import PeriodoMapper

class BuscarPeriodosImpl(BuscarPeriodos):

    @inject
    def __init__(self,
                 repository: PeriodoRepository,
                 mapper: PeriodoMapper):
        self._repo   = repository
        self._mapper = mapper

    def execute(self) -> List[PeriodoDTO]:
        dominios = self._repo.obtener_todos()
        return [ self._mapper.to_dto(p) for p in dominios ]
