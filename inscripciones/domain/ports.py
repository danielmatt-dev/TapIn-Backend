from abc import ABC, abstractmethod
from typing import List
from inscripciones.domain.inscripcion import Inscripcion

class InscripcionRepository(ABC):

    @abstractmethod
    def registrar(self, inscripcion: Inscripcion) -> Inscripcion:
        pass

    @abstractmethod
    def buscar_por_alumno(self, id_alumno: str) -> List[Inscripcion]:
        pass

    @abstractmethod
    def actualizar_periodo(self, id_inscripcion: str, nuevo_periodo: str) -> bool:
        pass

    @abstractmethod
    def vaciar_por_periodo(self, id_periodo: str) -> int:
        pass
