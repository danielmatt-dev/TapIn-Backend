from alertas.domain.alerta import Alerta
from alertas.domain.alerta_port import AlertaRepository
from alertas.infraestructure.alerta_model import AlertaModel


class AlertaRepositoryImpl(AlertaRepository):

    def buscar_por_id(self, id_alerta) -> Alerta | None:
        model = AlertaModel.objects.filter(id_alerta=id_alerta).first()
        if model is None:
            return None

        return Alerta(
            id_alerta=model.id_alerta,
            titulo=model.titulo,
            descripcion=model.descripcion,
            tipo=model.tipo
        )
