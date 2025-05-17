from abc import ABC, abstractmethod
from typing import List
from inscripciones.domain.dtos import InscripcionDTO
from inscripciones.infrastructure.inscripcion_model import InscripcionModel
from inscripciones.domain.dtos import DatosCompletosDTO


class NuevaInscripcion(ABC):
    @abstractmethod
    def execute(self, dto: InscripcionDTO) -> InscripcionDTO:
        pass

class BuscarInscripciones(ABC):
    @abstractmethod
    def execute(self, id_alumno: str) -> List[InscripcionModel]:
        pass

class ActualizarPeriodo(ABC):
    @abstractmethod
    def execute(self, id_inscripcion: str, id_periodo: str) -> bool:
        pass

class ObtenerDatos(ABC):
    @abstractmethod
    def execute(self) -> DatosCompletosDTO:
        ...