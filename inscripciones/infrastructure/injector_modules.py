from injector import Module, singleton, provider
from inscripciones.domain.ports import InscripcionRepository
from inscripciones.infrastructure.mapper.inscripcion_mapper import InscripcionMapper
from inscripciones.infrastructure.mapper.inscripcion_mapper_impl import InscripcionMapperImpl
from inscripciones.infrastructure.repositories import InscripcionRepositoryImpl
from inscripciones.application.use_cases.use_cases import (
    NuevaInscripcion, BuscarInscripciones,
    ActualizarPeriodo, VaciarInscripciones
)
from inscripciones.application.use_cases.impl.nueva_inscripcion_impl import NuevaInscripcionImpl
from inscripciones.application.use_cases.impl.buscar_inscripciones_impl import BuscarInscripcionesImpl
from inscripciones.application.use_cases.impl.actualizar_periodo_impl import ActualizarPeriodoImpl
from inscripciones.application.use_cases.impl.vaciar_inscripciones_impl import VaciarInscripcionesImpl

class InscripcionesInjectorModule(Module):

    @singleton
    @provider
    def provide_mapper(self) -> InscripcionMapper:
        return InscripcionMapperImpl()

    @singleton
    @provider
    def provide_repository(self) -> InscripcionRepository:
        return InscripcionRepositoryImpl(self.provide_mapper())

    @singleton
    @provider
    def provide_nueva_inscripcion(self) -> NuevaInscripcion:
        return NuevaInscripcionImpl(
            repository=self.provide_repository(),
            mapper=self.provide_mapper()
        )

    @singleton
    @provider
    def provide_buscar_inscripciones(self) -> BuscarInscripciones:
        return BuscarInscripcionesImpl(
            repository=self.provide_repository(),
            mapper=self.provide_mapper()
        )

    @singleton
    @provider
    def provide_actualizar_periodo(self) -> ActualizarPeriodo:
        return ActualizarPeriodoImpl(
            repository=self.provide_repository()
        )

    @singleton
    @provider
    def provide_vaciar_inscripciones(self) -> VaciarInscripciones:
        return VaciarInscripcionesImpl(
            repository=self.provide_repository()
        )
