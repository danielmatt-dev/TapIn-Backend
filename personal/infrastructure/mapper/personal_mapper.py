from abc import ABC, abstractmethod
from personal.domain.personal import Personal
from personal.domain.dtos import PersonalDTO
from personal.infrastructure.personal_model import PersonalModel

class PersonalMapper(ABC):

    @abstractmethod
    def to_domain(self, model: PersonalModel) -> Personal:
        pass

    @abstractmethod
    def to_model(self, domain: Personal) -> PersonalModel:
        pass

    @abstractmethod
    def to_dto(self, domain: Personal) -> PersonalDTO:
        pass
