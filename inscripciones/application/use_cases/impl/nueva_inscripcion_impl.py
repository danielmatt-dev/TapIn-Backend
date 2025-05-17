# inscripciones/application/use_cases/impl/nueva_inscripcion_impl.py
from inscripciones.application.use_cases.use_cases import NuevaInscripcion
from inscripciones.domain.inscripcion import Inscripcion
from inscripciones.domain.dtos import InscripcionDTO
from inscripciones.infrastructure.repositories import InscripcionRepository
from inscripciones.infrastructure.mapper.inscripcion_mapper import InscripcionMapper
from inscripciones.infrastructure.inscripcion_model import InscripcionModel


class NuevaInscripcionImpl(NuevaInscripcion):
    def __init__(self,
                 repository: InscripcionRepository,
                 mapper: InscripcionMapper):
        self._repository = repository
        self._mapper     = mapper

    def execute(self, dto: InscripcionDTO) -> InscripcionModel:
        entidad = Inscripcion(
            id_inscripcion=dto.id_inscripcion,
            alumno=dto.alumno,
            periodo=dto.periodo,
            fecha=dto.fecha,
            grado=dto.grado,
            grupo=dto.grupo,
            estado=dto.estado,
        )
        # ahora registrar() devuelve directamente el InscripcionModel
        return self._repository.registrar(entidad)
