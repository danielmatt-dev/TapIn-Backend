from injector import Module, singleton, provider

# Periodos
from periodos.domain.ports import PeriodoRepository
from periodos.infrastructure.mapper.periodo_mapper import PeriodoMapper
from periodos.infrastructure.mapper.periodo_mapper_impl import PeriodoMapperImpl
from periodos.infrastructure.repositories import PeriodoRepositoryImpl
from periodos.application.use_cases.use_cases import RegistrarPeriodo, BuscarPeriodos, EliminarPeriodo, ConsultarPeriodo
from periodos.application.use_cases.impl.registrar_periodo_impl import RegistrarPeriodoImpl
from periodos.application.use_cases.impl.buscar_periodos_impl import BuscarPeriodosImpl
from periodos.application.use_cases.impl.eliminar_periodo_impl import EliminarPeriodoImpl
from periodos.application.use_cases.impl.consultar_periodo_impl import ConsultarPeriodoImpl


# Bloques (para la composición de periodos con sus bloques)
from bloques.domain.ports import BloqueRepository
from bloques.infrastructure.mapper.bloque_mapper import BloqueMapper
from bloques.infrastructure.mapper.bloque_mapper_impl import BloqueMapperImpl
from bloques.infrastructure.repositories import BloqueRepositoryImpl


class PeriodosInjectorModule(Module):

    @singleton
    @provider
    def provide_periodo_mapper(self) -> PeriodoMapper:
        return PeriodoMapperImpl()

    @singleton
    @provider
    def provide_periodo_repository(self) -> PeriodoRepository:
        return PeriodoRepositoryImpl(self.provide_periodo_mapper())

    @singleton
    @provider
    def provide_bloque_mapper(self) -> BloqueMapper:
        return BloqueMapperImpl()

    @singleton
    @provider
    def provide_bloque_repository(self) -> BloqueRepository:
        return BloqueRepositoryImpl(self.provide_bloque_mapper())

    @singleton
    @provider
    def provide_registrar_periodo(self) -> RegistrarPeriodo:
        return RegistrarPeriodoImpl(
            repository=self.provide_periodo_repository(),
            mapper=self.provide_periodo_mapper()
        )

    @singleton
    @provider
    def provide_buscar_periodos(self) -> BuscarPeriodos:
        return BuscarPeriodosImpl(
            periodo_repository=self.provide_periodo_repository(),
            bloque_repository=self.provide_bloque_repository(),
            bloque_mapper=self.provide_bloque_mapper()
        )

    @singleton
    @provider
    def provide_eliminar_periodo(self) -> EliminarPeriodo:
        return EliminarPeriodoImpl(
            repository=self.provide_periodo_repository()
        )

    @singleton
    @provider
    def provide_consultar_periodo(self) -> ConsultarPeriodo:
        return ConsultarPeriodoImpl(
            periodo_repo=self.provide_periodo_repository(),
            bloque_repo=self.provide_bloque_repository(),
            bloque_mapper=self.provide_bloque_mapper()
        )