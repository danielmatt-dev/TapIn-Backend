from alertas.domain.alerta_port import AlertaRepository
from alertas.infraestructure.alerta_model import AlertaModel


class AlertaRepositoryImpl(AlertaRepository):

    def buscar_por_id(self, id_alerta) -> AlertaModel:
        return AlertaModel.objects.filter(id_alerta=id_alerta).first()