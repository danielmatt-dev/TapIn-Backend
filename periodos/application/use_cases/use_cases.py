from abc import ABC, abstractmethod
from typing import List
from periodos.domain.dtos import PeriodoDTO

class RegistrarPeriodo(ABC):
    @abstractmethod
    def execute(self, dto: PeriodoDTO) -> PeriodoDTO: ...

class BuscarPeriodos(ABC):
    @abstractmethod
    def execute(self) -> List[PeriodoDTO]: ...
