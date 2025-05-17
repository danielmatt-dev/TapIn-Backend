# inscripciones/application/use_cases/impl/actualizar_periodo_impl.py

from inscripciones.application.use_cases.use_cases import ActualizarPeriodo
from inscripciones.domain.ports import InscripcionRepository
from periodos.domain.periodo import Periodo

class ActualizarPeriodoImpl(ActualizarPeriodo):
    def __init__(self, repository: InscripcionRepository):
        self._repository = repository

    def execute(self, id_inscripcion: str, periodo: Periodo) -> bool:
        return self._repository.actualizar_periodo(
            id_inscripcion,
            periodo.id_periodo
        )
