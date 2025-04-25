from abc import ABC, abstractmethod

from alumnos.domain.alumno import Alumno


class RegistrarAlumno(ABC):

    @abstractmethod
    def execute(self, dto: any) -> Alumno:
        pass


class SilenciarAlumno(ABC):

    @abstractmethod
    def execute(self, id_alumno: str) -> bool:
        pass
