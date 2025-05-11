from inscripciones.infrastructure.mapper.inscripcion_mapper import InscripcionMapper
from inscripciones.infrastructure.inscripcion_model import InscripcionModel
from inscripciones.domain.inscripcion import Inscripcion
from inscripciones.domain.dtos import InscripcionDTO

class InscripcionMapperImpl(InscripcionMapper):

    def to_domain(self, model: InscripcionModel) -> Inscripcion:
        return Inscripcion(
            id_inscripcion=model.id_inscripcion,
            id_alumno=model.id_alumno,
            id_periodo=model.id_periodo,
            fecha=model.fecha,
            grado=model.grado,
            grupo=model.grupo,
            estado=model.estado
        )

    def to_model(self, domain: Inscripcion) -> InscripcionModel:
        return InscripcionModel(
            id_inscripcion=domain.id_inscripcion,
            id_alumno=domain.id_alumno,
            id_periodo=domain.id_periodo,
            fecha=domain.fecha,
            grado=domain.grado,
            grupo=domain.grupo,
            estado=domain.estado
        )

    def to_dto(self, domain: Inscripcion) -> InscripcionDTO:
        return InscripcionDTO(
            id_inscripcion=domain.id_inscripcion,
            id_alumno=domain.id_alumno,
            id_periodo=domain.id_periodo,
            fecha=domain.fecha,
            grado=domain.grado,
            grupo=domain.grupo,
            estado=domain.estado
        )
