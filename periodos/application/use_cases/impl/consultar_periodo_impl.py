from injector import inject
from typing import List
from periodos.application.use_cases.use_cases import ConsultarPeriodo
from periodos.domain.dtos import PeriodoDTO
from periodos.domain.ports import PeriodoRepository
from bloques.domain.ports import BloqueRepository
from bloques.infrastructure.mapper.bloque_mapper import BloqueMapper

class ConsultarPeriodoImpl(ConsultarPeriodo):
    @inject
    def __init__(
        self,
        periodo_repo: PeriodoRepository,
        bloque_repo: BloqueRepository,
        bloque_mapper: BloqueMapper
    ):
        self._periodo_repo = periodo_repo
        self._bloque_repo  = bloque_repo
        self._bloque_map   = bloque_mapper

    def execute(self, id_periodo: str) -> PeriodoDTO:
        p = self._periodo_repo.obtener_por_id(id_periodo)
        if p is None:
            raise Exception(f"Periodo {id_periodo} no encontrado")

        bloques = self._bloque_repo.obtener_por_periodo(id_periodo)
        bloques_dto = [self._bloque_map.to_dto(b) for b in bloques]

        return PeriodoDTO(
            id_periodo   = p.id_periodo,
            nombre       = p.nombre,
            hora_entrada = p.hora_entrada,
            hora_salida  = p.hora_salida,
            fecha_inicio = p.fecha_inicio,
            fecha_final  = p.fecha_final,
            estado       = p.estado,
            bloques      = bloques_dto
        )
