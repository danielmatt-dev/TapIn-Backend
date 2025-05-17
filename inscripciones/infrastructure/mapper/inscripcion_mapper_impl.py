from inscripciones.domain.inscripcion import Inscripcion
from inscripciones.domain.dtos import InscripcionDTO
from inscripciones.infrastructure.inscripcion_model import InscripcionModel
from inscripciones.infrastructure.mapper.inscripcion_mapper import InscripcionMapper
from alumnos.infrastructure.mapper.alumno_mapper_impl import AlumnoMapperImpl
from periodos.infrastructure.mapper.periodo_mapper_impl import PeriodoMapperImpl

class InscripcionMapperImpl(InscripcionMapper):
    def __init__(self):
        self._alumno_map  = AlumnoMapperImpl()
        self._periodo_map = PeriodoMapperImpl()

    def to_domain(self, model: InscripcionModel) -> Inscripcion:
        return Inscripcion(
            id_inscripcion=model.id_inscripcion,
            alumno=self._alumno_map.to_domain(model.alumno),
            periodo=self._periodo_map.to_domain(model.periodo),
            fecha=model.fecha,
            grado=model.grado or '',
            grupo=model.grupo or '',
            estado=model.estado
        )

    def to_model(self, domain: Inscripcion) -> InscripcionModel:
        m = InscripcionModel(
            id_inscripcion=domain.id_inscripcion,
            fecha=domain.fecha,
            grado=domain.grado,
            grupo=domain.grupo,
            estado=domain.estado
        )
        m.alumno_id  = domain.alumno.id_alumno
        m.periodo_id = domain.periodo.id_periodo
        return m

    def to_dto(self, domain: Inscripcion) -> InscripcionDTO:
        return InscripcionDTO(
            id_inscripcion=domain.id_inscripcion,
            alumno=self._alumno_map.to_dto(domain.alumno),
            periodo=self._periodo_map.to_dto(domain.periodo),
            fecha=domain.fecha,
            grado=domain.grado,
            grupo=domain.grupo,
            estado=domain.estado
        )
