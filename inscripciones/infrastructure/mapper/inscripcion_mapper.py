from abc import ABC, abstractmethod
from inscripciones.domain.inscripcion import Inscripcion
from inscripciones.domain.dtos import InscripcionDTO
from inscripciones.infrastructure.inscripcion_model import InscripcionModel

class InscripcionMapper(ABC):

    @abstractmethod
    def to_domain(self, model: InscripcionModel) -> Inscripcion:
        pass

    @abstractmethod
    def to_model(self, domain: Inscripcion) -> InscripcionModel:
        pass

    @abstractmethod
    def to_dto(self, domain: Inscripcion) -> InscripcionDTO:
        pass
