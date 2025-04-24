from injector import Module, singleton, provider

from alumnos.application.use_cases.impl.registrar_alumno_impl import RegistrarAlumnoImpl
from alumnos.application.use_cases.use_cases import RegistrarAlumno
from alumnos.domain.ports import AlumnoRepository
from alumnos.infrastructure.mapper.alumno_mapper import AlumnoMapper
from alumnos.infrastructure.mapper.alumno_mapper_impl import AlumnoMapperImpl
from alumnos.infrastructure.repositories import AlumnoRepositoryImpl


class InjectorModule(Module):

    @singleton
    @provider
    def provide_mapper(self) -> AlumnoMapper:
        return AlumnoMapperImpl()

    @singleton
    @provider
    def provide_alumno_repository(self) -> AlumnoRepository:
        return AlumnoRepositoryImpl(self.provide_mapper)

    @singleton
    @provider
    def provide_registrar_alumo(self) -> RegistrarAlumno:
        return RegistrarAlumnoImpl(self.provide_alumno_repository)
