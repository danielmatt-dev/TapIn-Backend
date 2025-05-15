from injector import inject
from typing import List

from periodos.domain.periodo import Periodo
from periodos.infrastructure.periodo_model import PeriodoModel
from periodos.domain.ports import PeriodoRepository
from periodos.infrastructure.mapper.periodo_mapper import PeriodoMapper


class PeriodoRepositoryImpl(PeriodoRepository):

    @inject
    def __init__(self, mapper: PeriodoMapper):
        self._mapper = mapper

    def registrar(self, periodo: Periodo) -> Periodo:
        model = self._mapper.to_model(periodo)
        model.save()
        return self._mapper.to_domain(model)

    def obtener_todos(self) -> List[Periodo]:
        qs = PeriodoModel.objects.all()
        return [self._mapper.to_domain(m) for m in qs]

    def eliminar(self, id_periodo: str) -> bool:
        deleted, _ = PeriodoModel.objects.filter(id_periodo=id_periodo).delete()
        return bool(deleted)
