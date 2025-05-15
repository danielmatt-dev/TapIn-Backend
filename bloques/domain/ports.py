from abc import ABC, abstractmethod
from typing import List
from bloques.domain.bloque import Bloque

class BloqueRepository(ABC):
    @abstractmethod
    def registrar(self, bloque: Bloque) -> Bloque:
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Bloque]:
        pass

    @abstractmethod
    def eliminar(self, id_bloque: str) -> bool:
        pass
    @abstractmethod
    def obtener_por_periodo(self, id_periodo: str) -> List[Bloque]:
        pass