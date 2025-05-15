from abc import ABC, abstractmethod

from periodos.domain.periodo import Periodo
from periodos.domain.dtos import PeriodoDTO
from periodos.infrastructure.periodo_model import PeriodoModel


class PeriodoMapper(ABC):

    @abstractmethod
    def to_domain(self, model: PeriodoModel) -> Periodo: ...

    @abstractmethod
    def to_model(self, domain: Periodo) -> PeriodoModel: ...

    @abstractmethod
    def to_dto(self, domain: Periodo) -> PeriodoDTO: ...

    @abstractmethod
    def to_domain_from_dto(self, dto: PeriodoDTO) -> Periodo: ...
