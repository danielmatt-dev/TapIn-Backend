from abc import ABC, abstractmethod
from datetime import date
from typing import List

from asistencia.domain.dtos import AsistenciaDTO, AsistenciasDTO, AsistenciaResponse


class RegistrarAsistencia(ABC):
    @abstractmethod
    def execute(self, dto: AsistenciaDTO) -> AsistenciaDTO:
        pass

class BuscarAsistencias(ABC):
    @abstractmethod
    def execute(self, id_alumno: str) -> List[AsistenciaDTO]:
        pass

class ConsultarAsistenciasDelDia(ABC):
    @abstractmethod
    def execute(self, fecha: date) -> List[AsistenciaDTO]:
        pass

class ConsultarAsistenciasDelPeriodo(ABC):
    @abstractmethod
    def execute(self, fecha_inicio: date, fecha_fin: date) -> List[AsistenciaResponse]:
        pass
