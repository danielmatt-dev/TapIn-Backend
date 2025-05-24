from injector import Module, singleton, provider

from personal.application.use_cases.impl.buscar_todo_personal_impl import BuscarPersonalPorCorreoImpl
from personal.application.use_cases.impl.registrar_personal_impl import RegistrarPersonalImpl
from personal.application.use_cases.impl.eliminar_personal_impl import EliminarPersonalImpl
from personal.application.use_cases.impl.consultar_estado_personal_impl import ConsultarEstadoPersonalImpl
from personal.application.use_cases.impl.actualizar_personal_impl import ActualizarPersonalImpl

from personal.domain.ports import PersonalRepository
from personal.infrastructure.mapper.personal_mapper import PersonalMapper
from personal.infrastructure.mapper.personal_mapper_impl import PersonalMapperImpl
from personal.infrastructure.repositories import PersonalRepositoryImpl

from personal.application.use_cases.use_cases import (
    RegistrarPersonal, EliminarPersonal,
    ConsultarEstadoPersonal, ActualizarPersonal, BuscarPersonalPorCorreo
)

class PersonalInjectorModule(Module):

    @singleton
    @provider
    def provide_mapper(self) -> PersonalMapper:
        return PersonalMapperImpl()

    @singleton
    @provider
    def provide_repository(self) -> PersonalRepository:
        return PersonalRepositoryImpl(self.provide_mapper())

    @singleton
    @provider
    def provide_registrar(self) -> RegistrarPersonal:
        return RegistrarPersonalImpl(
            repository=self.provide_repository(),
            mapper=self.provide_mapper()
        )

    @singleton
    @provider
    def provide_eliminar(self) -> EliminarPersonal:
        return EliminarPersonalImpl(repository=self.provide_repository())

    @singleton
    @provider
    def provide_consultar_estado(self) -> ConsultarEstadoPersonal:
        return ConsultarEstadoPersonalImpl(
            repository=self.provide_repository(),
            mapper=self.provide_mapper()
        )

    @singleton
    @provider
    def provide_actualizar(self) -> ActualizarPersonal:
        return ActualizarPersonalImpl(
            repository=self.provide_repository(),
            mapper=self.provide_mapper()
        )

    @singleton
    @provider
    def provide_buscar_personal_correo(self) -> BuscarPersonalPorCorreo:
        return BuscarPersonalPorCorreoImpl(
            repository=self.provide_repository(),
            mapper=self.provide_mapper()
        )
