from injector import inject

from periodos.application.use_cases.use_cases import EliminarPeriodo
from periodos.domain.ports import PeriodoRepository


class EliminarPeriodoImpl(EliminarPeriodo):

    @inject
    def __init__(self, repository: PeriodoRepository):
        self._repository = repository

    def execute(self, id_periodo: str) -> bool:
        return self._repository.eliminar(id_periodo)
