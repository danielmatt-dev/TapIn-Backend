from injector import inject
from inscripciones.application.use_cases.use_cases import VaciarInscripciones
from inscripciones.domain.ports import InscripcionRepository

class VaciarInscripcionesImpl(VaciarInscripciones):

    @inject
    def __init__(self, repository: InscripcionRepository):
        self._repo = repository

    def execute(self, id_periodo: str) -> int:
        return self._repo.vaciar_por_periodo(id_periodo)
