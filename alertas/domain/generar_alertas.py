from typing import List

from alertas.domain.alerta import Alerta
from asistencia.domain.dtos import AsistenciaResponse


class GenerarAlertas:

    def execute(self, asistencias: List[AsistenciaResponse]) -> List[Alerta]:
        return []
