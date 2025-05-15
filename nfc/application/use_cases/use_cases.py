from abc import ABC, abstractmethod
from typing import List
from nfc.domain.dtos import NFCDTO

class RegistrarNFC(ABC):
    @abstractmethod
    def execute(self, dto: NFCDTO) -> NFCDTO: ...

class EliminarNFC(ABC):
    @abstractmethod
    def execute(self, id_nfc: int) -> bool: ...

class ListarNFC(ABC):
    @abstractmethod
    def execute(self) -> List[NFCDTO]: ...

class ActualizarEstadoNFC(ABC):
    @abstractmethod
    def execute(self, id_nfc: int, estado: str) -> bool: ...
