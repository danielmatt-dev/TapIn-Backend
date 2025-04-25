from abc import ABC, abstractmethod

from alumnos.domain.alumno import Alumno
from alumnos.infrastructure.alumno_model import AlumnoModel


class AlumnoMapper(ABC):

    @abstractmethod
    def toDomain(self, model: AlumnoModel) -> Alumno:
        pass

    @abstractmethod
    def toModel(self, domain: Alumno) -> AlumnoModel:
        pass
