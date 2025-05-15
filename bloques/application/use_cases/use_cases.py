from abc import ABC, abstractmethod
from typing import List
from bloques.domain.dtos import BloqueDTO

class RegistrarBloque(ABC):
    @abstractmethod
    def execute(self, dto: BloqueDTO) -> BloqueDTO:
        pass

class BuscarBloques(ABC):
    @abstractmethod
    def execute(self) -> List[BloqueDTO]:
        pass

class EliminarBloque(ABC):
    @abstractmethod
    def execute(self, id_bloque: str) -> bool:
        pass
