from abc import ABC, abstractmethod
from typing import List
from inscripciones.domain.dtos import InscripcionDTO

class NuevaInscripcion(ABC):
    @abstractmethod
    def execute(self, dto: InscripcionDTO) -> InscripcionDTO:
        pass

class BuscarInscripciones(ABC):
    @abstractmethod
    def execute(self, id_alumno: str) -> List[InscripcionDTO]:
        pass

class ActualizarPeriodo(ABC):
    @abstractmethod
    def execute(self, id_inscripcion: str, id_periodo: str) -> bool:
        pass

class VaciarInscripciones(ABC):
    @abstractmethod
    def execute(self) -> bool:
        pass
