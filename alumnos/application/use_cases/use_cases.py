from abc import ABC, abstractmethod
from typing import List

from alumnos.domain.dtos import AlumnoDTO


class RegistrarAlumno(ABC):

    @abstractmethod
    def execute(self, dto: AlumnoDTO) -> AlumnoDTO:
        pass


class SilenciarAlumno(ABC):

    @abstractmethod
    def execute(self, id_alumno: str) -> bool:
        pass
    
class EliminarAlumno(ABC):

    @abstractmethod
    def execute(self, id_alumno: str) -> bool:
        pass

class ConsultarEstadoAlumnos(ABC):

    @abstractmethod
    def execute(self) -> List[AlumnoDTO]:
        pass

class ActualizarAlumno(ABC):

    @abstractmethod
    def execute(self, dto: AlumnoDTO) -> AlumnoDTO:
        pass