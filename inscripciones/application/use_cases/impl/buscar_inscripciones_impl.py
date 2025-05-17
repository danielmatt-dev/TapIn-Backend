from injector import inject
from typing import List
from inscripciones.application.use_cases.use_cases import BuscarInscripciones
from inscripciones.domain.ports import InscripcionRepository
from inscripciones.infrastructure.inscripcion_model import InscripcionModel

class BuscarInscripcionesImpl(BuscarInscripciones):
    def __init__(self,
                 repository: InscripcionRepository):
        self._repository = repository

    def execute(self, id_alumno: str) -> List[InscripcionModel]:
        # Devuelve directamente los modelos Django
        return self._repository.buscar_por_alumno(id_alumno)