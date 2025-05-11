from injector import Module, singleton, provider

from periodos.domain.ports import PeriodoRepository
from periodos.infrastructure.mapper.periodo_mapper import PeriodoMapper
from periodos.infrastructure.mapper.periodo_mapper_impl import PeriodoMapperImpl
from periodos.infrastructure.repositories import PeriodoRepositoryImpl
from periodos.application.use_cases.use_cases import RegistrarPeriodo, BuscarPeriodos
from periodos.application.use_cases.impl.registrar_periodo_impl import RegistrarPeriodoImpl
from periodos.application.use_cases.impl.buscar_periodos_impl import BuscarPeriodosImpl

class PeriodosInjectorModule(Module):

    @singleton
    @provider
    def provide_mapper(self) -> PeriodoMapper:
        return PeriodoMapperImpl()

    @singleton
    @provider
    def provide_repository(self) -> PeriodoRepository:
        return PeriodoRepositoryImpl(self.provide_mapper())

    @singleton
    @provider
    def provide_registrar_periodo(self) -> RegistrarPeriodo:
        return RegistrarPeriodoImpl(
            repository=self.provide_repository(),
            mapper=self.provide_mapper()
        )

    @singleton
    @provider
    def provide_buscar_periodos(self) -> BuscarPeriodos:
        return BuscarPeriodosImpl(
            repository=self.provide_repository(),
            mapper=self.provide_mapper()
        )
