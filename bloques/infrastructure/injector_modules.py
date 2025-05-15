from injector import Module, singleton, provider

# repositorio y mapper de bloques
from bloques.domain.ports import BloqueRepository
from bloques.infrastructure.mapper.bloque_mapper import BloqueMapper
from bloques.infrastructure.mapper.bloque_mapper_impl import BloqueMapperImpl
from bloques.infrastructure.repositories import BloqueRepositoryImpl

# casos de uso
from bloques.application.use_cases.use_cases import (
    RegistrarBloque, BuscarBloques, EliminarBloque
)
from bloques.application.use_cases.impl.registrar_bloque_impl import RegistrarBloqueImpl
from bloques.application.use_cases.impl.buscar_bloques_impl import BuscarBloquesImpl
from bloques.application.use_cases.impl.eliminar_bloque_impl import EliminarBloqueImpl

# repositorio de periodos
from periodos.domain.ports import PeriodoRepository
from periodos.infrastructure.mapper.periodo_mapper import PeriodoMapper
from periodos.infrastructure.mapper.periodo_mapper_impl import PeriodoMapperImpl
from periodos.infrastructure.repositories import PeriodoRepositoryImpl

class BloquesInjectorModule(Module):

    @singleton
    @provider
    def provide_mapper(self) -> BloqueMapper:
        return BloqueMapperImpl()

    @singleton
    @provider
    def provide_repository(self) -> BloqueRepository:
        return BloqueRepositoryImpl(self.provide_mapper())

    @singleton
    @provider
    def provide_registrar_bloque(self) -> RegistrarBloque:
        return RegistrarBloqueImpl(
            repository=self.provide_repository(),
            mapper=self.provide_mapper()
        )

    @singleton
    @provider
    def provide_buscar_bloques(self) -> BuscarBloques:
        return BuscarBloquesImpl(
            repository=self.provide_repository(),
            mapper=self.provide_mapper()
        )

    @singleton
    @provider
    def provide_eliminar_bloque(self) -> EliminarBloque:
        return EliminarBloqueImpl(
            repository=self.provide_repository()
        )