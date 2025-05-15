from abc import ABC, abstractmethod
from typing import List

from periodos.domain.periodo import Periodo


class PeriodoRepository(ABC):
    @abstractmethod
    def registrar(self, periodo: Periodo) -> Periodo: ...

    @abstractmethod
    def obtener_todos(self) -> List[Periodo]: ...

    @abstractmethod
    def eliminar(self, id_periodo: str) -> bool: ...
    
    def obtener_por_id(self, id_periodo: str) -> Periodo | None:
        pass