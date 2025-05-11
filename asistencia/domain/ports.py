from abc import ABC, abstractmethod
from datetime import date
from typing import List, Optional

from asistencia.domain.asistencia import Asistencia

class AsistenciaRepository(ABC):

    @abstractmethod
    def registrar(self, a: Asistencia) -> Asistencia:
        pass

    @abstractmethod
    def buscar_por_alumno(self, id_alumno: str) -> List[Asistencia]:
        pass

    @abstractmethod
    def consultar_por_dia(self, fecha: date) -> List[Asistencia]:
        pass

    @abstractmethod
    def consultar_por_periodo(self, fecha_inicio: date, fecha_fin: date) -> List[Asistencia]:
        pass
