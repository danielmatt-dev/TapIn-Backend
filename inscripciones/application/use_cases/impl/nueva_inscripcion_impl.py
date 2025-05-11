from injector import inject
from inscripciones.application.use_cases.use_cases import NuevaInscripcion
from inscripciones.domain.dtos import InscripcionDTO
from inscripciones.domain.inscripcion import Inscripcion
from inscripciones.domain.ports import InscripcionRepository
from inscripciones.infrastructure.mapper.inscripcion_mapper import InscripcionMapper

class NuevaInscripcionImpl(NuevaInscripcion):

    @inject
    def __init__(self,
                 repository: InscripcionRepository,
                 mapper: InscripcionMapper):
        self._repository = repository
        self._mapper = mapper

    def execute(self, dto: InscripcionDTO) -> InscripcionDTO:
        entidad = Inscripcion(
            id_inscripcion=dto.id_inscripcion,
            id_alumno=dto.id_alumno,
            id_periodo=dto.id_periodo,
            fecha=dto.fecha,
            grado=dto.grado,
            grupo=dto.grupo,
            estado=dto.estado,
        )
        creado = self._repository.registrar(entidad)
        return self._mapper.to_dto(creado)
