from abc import ABC

from alumnos.domain.alumno import Alumno
from alumnos.infrastructure.alumno_model import AlumnoModel

from alumnos.infrastructure.mapper.alumno_mapper import AlumnoMapper


class AlumnoMapperImpl(AlumnoMapper, ABC):

    def toDomain(self, model: AlumnoModel) -> Alumno:
        return Alumno(model.nombre_completo)

    def toModel(self, domain: Alumno) -> AlumnoModel:
        return AlumnoModel(domain.nombre)

