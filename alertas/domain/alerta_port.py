from abc import ABC, abstractmethod

from alertas.domain.alerta import Alerta


class AlertaRepository(ABC):

    @abstractmethod
    def buscar_por_id(self, id_alerta:int) -> Alerta | None:
        pass
