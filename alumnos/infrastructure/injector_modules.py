from injector import Module, singleton, provider

from alumnos.application.use_cases.impl.registrar_alumno_impl import RegistrarAlumnoImpl
from alumnos.domain.ports import AlumnoRepository
from alumnos.infrastructure.mapper.alumno_mapper import AlumnoMapper
from alumnos.infrastructure.mapper.alumno_mapper_impl import AlumnoMapperImpl
from alumnos.infrastructure.repositories import AlumnoRepositoryImpl
from alumnos.application.use_cases.use_cases import RegistrarAlumno, SilenciarAlumno, EliminarAlumno, ConsultarEstadoAlumnos, ActualizarAlumno
from alumnos.application.use_cases.impl.silenciar_alumno_impl import SilenciarAlumnoImpl
from alumnos.application.use_cases.impl.eliminar_alumno_impl import EliminarAlumnoImpl
from alumnos.application.use_cases.impl.consultar_estado_alumnos_impl import ConsultarEstadoAlumnosImpl
from alumnos.application.use_cases.impl.actualizar_alumnos_impl import ActualizarAlumnoImpl


class InjectorModule(Module):

    @singleton
    @provider
    def provide_mapper(self) -> AlumnoMapper:
        return AlumnoMapperImpl()

    @singleton
    @provider
    def provide_alumno_repository(self) -> AlumnoRepository:
        return AlumnoRepositoryImpl(self.provide_mapper())

    @singleton
    @provider
    def provide_registrar_alumo(self) -> RegistrarAlumno:
        return RegistrarAlumnoImpl(repository=self.provide_alumno_repository(), mapper=self.provide_mapper())

    @singleton
    @provider
    def provide_silenciar_alumno(self) -> SilenciarAlumno:
        return SilenciarAlumnoImpl(repository=self.provide_alumno_repository())

    @singleton
    @provider
    def provide_eliminar_alumno(self) -> EliminarAlumno:
        return EliminarAlumnoImpl(repository=self.provide_alumno_repository())

    @singleton
    @provider
    def provide_consultar_estado_alumnos(self) -> ConsultarEstadoAlumnos:
        return ConsultarEstadoAlumnosImpl(
        repository=self.provide_alumno_repository(),
        mapper=self.provide_mapper()
    )
    
    @singleton
    @provider
    def provide_actualizar_alumno(self) -> ActualizarAlumno:
        return ActualizarAlumnoImpl(
            repository=self.provide_alumno_repository(),
            mapper=self.provide_mapper()
        )