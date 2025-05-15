from abc import ABC, abstractmethod
from bloques.domain.bloque import Bloque
from bloques.domain.dtos import BloqueDTO
from bloques.infrastructure.bloque_model import BloqueModel

class BloqueMapper(ABC):
    @abstractmethod
    def to_domain(self, model: BloqueModel) -> Bloque:
        pass

    @abstractmethod
    def to_model(self, domain: Bloque) -> BloqueModel:
        pass

    @abstractmethod
    def to_dto(self, domain: Bloque) -> BloqueDTO:
        pass
