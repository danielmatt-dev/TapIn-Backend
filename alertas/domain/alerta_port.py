from abc import ABC, abstractmethod

from alertas.infraestructure.alerta_model import AlertaModel


class AlertaRepository(ABC):

    @abstractmethod
    def buscar_por_id(self, id_alerta) -> AlertaModel:
        pass