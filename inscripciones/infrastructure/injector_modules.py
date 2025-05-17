# inscripciones/infrastructure/injector_modules.py

from injector import Module, singleton, provider

# Casos de uso
from inscripciones.application.use_cases.use_cases import (
    NuevaInscripcion, BuscarInscripciones, ActualizarPeriodo, ObtenerDatos
)
from inscripciones.application.use_cases.impl.nueva_inscripcion_impl import NuevaInscripcionImpl
from inscripciones.application.use_cases.impl.buscar_inscripciones_impl import BuscarInscripcionesImpl
from inscripciones.application.use_cases.impl.actualizar_periodo_impl import ActualizarPeriodoImpl
from inscripciones.application.use_cases.impl.obtener_datos_impl import ObtenerDatosImpl

# Repositorio y mapper de Inscripciones
from inscripciones.domain.ports import InscripcionRepository
from inscripciones.infrastructure.mapper.inscripcion_mapper import InscripcionMapper
from inscripciones.infrastructure.mapper.inscripcion_mapper_impl import InscripcionMapperImpl
from inscripciones.infrastructure.repositories import InscripcionRepositoryImpl

# Repositorio y mapper de Alumnos
from alumnos.domain.ports import AlumnoRepository
from alumnos.infrastructure.mapper.alumno_mapper_impl import AlumnoMapperImpl as AlumnoMapper
from alumnos.infrastructure.repositories import AlumnoRepositoryImpl

# Repositorio y mapper de Periodos
from periodos.domain.ports import PeriodoRepository
from periodos.infrastructure.mapper.periodo_mapper_impl import PeriodoMapperImpl as PeriodoMapper
from periodos.infrastructure.repositories import PeriodoRepositoryImpl


class InscripcionesInjectorModule(Module):

    @singleton
    @provider
    def provide_mapper(self) -> InscripcionMapper:
        
        return InscripcionMapperImpl()

    @singleton
    @provider
    def provide_inscripcion_repository(self) -> InscripcionRepository:
        return InscripcionRepositoryImpl(self.provide_mapper())

    @singleton
    @provider
    def provide_nueva_inscripcion(self) -> NuevaInscripcion:
        return NuevaInscripcionImpl(
            repository=self.provide_inscripcion_repository(),
            mapper=self.provide_mapper()
        )

    @singleton
    @provider
    def provide_buscar_inscripciones(self) -> BuscarInscripciones:
        return BuscarInscripcionesImpl(
            repository=self.provide_inscripcion_repository()
        )

    @singleton
    @provider
    def provide_actualizar_periodo(self) -> ActualizarPeriodo:
        return ActualizarPeriodoImpl(
            repository=self.provide_inscripcion_repository()
        )

    @singleton
    @provider
    def provide_alumno_repository(self) -> AlumnoRepository:
        # Inyecta el mapper de Alumno
        return AlumnoRepositoryImpl(AlumnoMapper())

    @singleton
    @provider
    def provide_periodo_repository(self) -> PeriodoRepository:
        # Inyecta el mapper de Periodo
        return PeriodoRepositoryImpl(PeriodoMapper())

    @singleton
    @provider
    def provide_obtener_datos(self) -> ObtenerDatos:
        return ObtenerDatosImpl(
            alumno_repo  = self.provide_alumno_repository(),
            insc_repo    = self.provide_inscripcion_repository(),
            periodo_repo = self.provide_periodo_repository()
        )
