from injector import inject
from periodos.application.use_cases.use_cases import RegistrarPeriodo
from periodos.domain.dtos import PeriodoDTO
from periodos.domain.periodo import Periodo
from periodos.domain.ports import PeriodoRepository
from periodos.infrastructure.mapper.periodo_mapper import PeriodoMapper

class RegistrarPeriodoImpl(RegistrarPeriodo):

    @inject
    def __init__(self,
                 repository: PeriodoRepository,
                 mapper: PeriodoMapper):
        self._repo   = repository
        self._mapper = mapper

    def execute(self, dto: PeriodoDTO) -> PeriodoDTO:
        # Construimos la entidad de dominio desde el DTO
        entidad = Periodo(
            id_periodo=dto.id_periodo,
            nombre=dto.nombre,
            hora_entrada=dto.hora_entrada,
            hora_salida=dto.hora_salida,
            fecha_inicio=dto.fecha_inicio,
            fecha_final=dto.fecha_final,
            estado=dto.estado
        )
        creado = self._repo.registrar(entidad)
        return self._mapper.to_dto(creado)
