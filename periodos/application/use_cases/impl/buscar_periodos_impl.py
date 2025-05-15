from injector import inject
from typing import List

from periodos.application.use_cases.use_cases import BuscarPeriodos
from periodos.domain.dtos import PeriodoDTO
from periodos.domain.ports import PeriodoRepository
from bloques.domain.ports import BloqueRepository
from bloques.infrastructure.mapper.bloque_mapper import BloqueMapper
from bloques.domain.dtos import BloqueDTO


class BuscarPeriodosImpl(BuscarPeriodos):

    @inject
    def __init__(self,
                 periodo_repository: PeriodoRepository,
                 bloque_repository: BloqueRepository,   # ya tiene obtener_por_periodo
                 bloque_mapper: BloqueMapper):
        self._periodo_repo = periodo_repository
        self._bloque_repo  = bloque_repository
        self._bloque_map   = bloque_mapper

    def execute(self) -> List[PeriodoDTO]:
        periodos = self._periodo_repo.obtener_todos()
        result = []

        for p in periodos:
            # ahora obtenemos sólo los bloques de ese periodo
            bloques = self._bloque_repo.obtener_por_periodo(p.id_periodo)
            bloques_dto = [self._bloque_map.to_dto(b) for b in bloques]

            result.append(
                PeriodoDTO(
                    id_periodo  = p.id_periodo,
                    nombre      = p.nombre,
                    hora_entrada= p.hora_entrada,
                    hora_salida = p.hora_salida,
                    fecha_inicio= p.fecha_inicio,
                    fecha_final = p.fecha_final,
                    estado      = p.estado,
                    bloques     = bloques_dto
                )
            )
        return result
