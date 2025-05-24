from abc import ABC, abstractmethod
from typing import List
from personal.domain.dtos import PersonalDTO

class RegistrarPersonal(ABC):
    @abstractmethod
    def execute(self, dto: PersonalDTO) -> PersonalDTO:
        pass

class EliminarPersonal(ABC):
    @abstractmethod
    def execute(self, id_personal: str) -> bool:
        pass

class ConsultarEstadoPersonal(ABC):
    @abstractmethod
    def execute(self) -> List[PersonalDTO]:
        pass

class ActualizarPersonal(ABC):
    @abstractmethod
    def execute(self, dto: PersonalDTO) -> PersonalDTO:
        pass


class BuscarPersonalPorCorreo(ABC):

    @abstractmethod
    def execute(self, correo: str) -> PersonalDTO:
        pass
