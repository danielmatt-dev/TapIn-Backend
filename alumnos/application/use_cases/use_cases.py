from abc import ABC, abstractmethod

from alumnos.domain.dtos import AlumnoDTO


class RegistrarAlumno(ABC):

    @abstractmethod
    def execute(self, dto: AlumnoDTO) -> AlumnoDTO:
        pass


class SilenciarAlumno(ABC):

    @abstractmethod
    def execute(self, id_alumno: str) -> bool:
        pass
