from injector import inject
from inscripciones.application.use_cases.use_cases import ActualizarPeriodo
from inscripciones.domain.ports import InscripcionRepository

class ActualizarPeriodoImpl(ActualizarPeriodo):

    @inject
    def __init__(self, repository: InscripcionRepository):
        self._repo = repository

    def execute(self, id_inscripcion: str, nuevo_periodo: str) -> bool:
        return self._repo.actualizar_periodo(id_inscripcion, nuevo_periodo)
