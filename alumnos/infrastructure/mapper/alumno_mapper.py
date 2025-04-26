from abc import ABC, abstractmethod

from alumnos.domain.alumno import Alumno
from alumnos.domain.dtos import AlumnoDTO
from alumnos.infrastructure.alumno_model import AlumnoModel


class AlumnoMapper(ABC):

    @abstractmethod
    def to_domain(self, model: AlumnoModel) -> Alumno:
        pass

    @abstractmethod
    def to_model(self, domain: Alumno) -> AlumnoModel:
        pass

    @abstractmethod
    def to_dto(self, domain: Alumno) -> AlumnoDTO:
        pass
