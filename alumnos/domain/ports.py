from abc import ABC, abstractmethod
from typing import Any, List

from alumnos.domain.alumno import Alumno


class AlumnoRepository(ABC):

    @abstractmethod
    def registrar(self, alumno: Alumno) -> Alumno:
        pass

    @abstractmethod
    def obtener_por_correo(self, correo: str) -> Alumno:
        pass
    
    @abstractmethod
    def obtener_por_id(self, id_alumno: str) -> Alumno:
        pass

    @abstractmethod
    def actualizar(self, alumno: Alumno) -> None:
        pass

    @abstractmethod
    def eliminar(self, id_alumno: str) -> bool:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Alumno]:
        pass