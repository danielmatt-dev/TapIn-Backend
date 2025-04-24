from abc import ABC, abstractmethod
from typing import Any

from alumnos.domain.alumno import Alumno


class AlumnoRepository(ABC):

    @abstractmethod
    def registrar(self, alumno: Alumno) -> Alumno:
        pass

    @abstractmethod
    def obtener_por_correo(self, correo: str) -> Alumno:
        pass
