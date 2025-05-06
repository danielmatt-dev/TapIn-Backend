from abc import ABC, abstractmethod
from asistencia.domain.asistencia import Asistencia
from asistencia.domain.dtos import AsistenciaDTO
from asistencia.infrastructure.asistencia_model import AsistenciaModel

class AsistenciaMapper(ABC):

    @abstractmethod
    def to_domain(self, model: AsistenciaModel) -> Asistencia:
        pass

    @abstractmethod
    def to_model(self, domain: Asistencia) -> AsistenciaModel:
        pass

    @abstractmethod
    def to_dto(self, domain: Asistencia) -> AsistenciaDTO:
        pass
