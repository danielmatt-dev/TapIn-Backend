from injector import inject
from inscripciones.application.use_cases.use_cases import VaciarInscripciones
from inscripciones.domain.ports import InscripcionRepository

class VaciarInscripcionesImpl(VaciarInscripciones):

    @inject
    def __init__(self, repository: InscripcionRepository):
        self._repository = repository

    def execute(self) -> bool:
        return self._repository.vaciar()
