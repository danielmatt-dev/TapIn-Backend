from abc import ABC, abstractmethod
from alumnos.domain.dtos import AlumnoDTO

class EnviarNotificacion(ABC):
    @abstractmethod
    def execute(self, id_nfc: int, id_notificacion: int) -> bool:
        pass

class EnviarAlerta(ABC):
    @abstractmethod
    def execute(self, alumno: AlumnoDTO, id_notificacion: int) -> bool:
        pass
