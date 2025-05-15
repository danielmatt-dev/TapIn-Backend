from injector import inject

from periodos.application.use_cases.use_cases import RegistrarPeriodo
from periodos.domain.dtos import PeriodoDTO
from periodos.domain.ports import PeriodoRepository
from periodos.infrastructure.mapper.periodo_mapper import PeriodoMapper


class RegistrarPeriodoImpl(RegistrarPeriodo):

    @inject
    def __init__(self,
                 repository: PeriodoRepository,
                 mapper: PeriodoMapper):
        self._repo = repository
        self._mapper = mapper

    def execute(self, dto: PeriodoDTO) -> PeriodoDTO:
        entidad = self._mapper.to_domain_from_dto(dto)
        creado = self._repo.registrar(entidad)
        return self._mapper.to_dto(creado)
