from injector import inject
from typing import List
from inscripciones.application.use_cases.use_cases import BuscarInscripciones
from inscripciones.domain.ports import InscripcionRepository
from inscripciones.infrastructure.mapper.inscripcion_mapper import InscripcionMapper
from inscripciones.domain.dtos import InscripcionDTO

class BuscarInscripcionesImpl(BuscarInscripciones):

    @inject
    def __init__(self,
                 repository: InscripcionRepository,
                 mapper: InscripcionMapper):
        self._repo   = repository
        self._mapper = mapper

    def execute(self, id_alumno: str) -> List[InscripcionDTO]:
        regs = self._repo.buscar_por_alumno(id_alumno)
        return [self._mapper.to_dto(r) for r in regs]
