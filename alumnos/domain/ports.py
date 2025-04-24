from abc import ABC, abstractmethod
from typing import Any

class AlumnoRepository(ABC):
    @abstractmethod
    def registrar(self, data: dict) -> Any:
        pass

    @abstractmethod
    def obtener_por_correo(self, correo: str) -> Any:
        pass
