from injector import Module, singleton, provider

from asistencia.infrastructure.mapper.asistencia_mapper import AsistenciaMapper
from asistencia.infrastructure.mapper.asistencia_mapper_impl import AsistenciaMapperImpl
from asistencia.application.use_cases.impl.registrar_asistencia_impl import RegistrarAsistenciaImpl
from asistencia.application.use_cases.impl.buscar_asistencias_impl import BuscarAsistenciasImpl
from asistencia.application.use_cases.impl.consultar_asistencias_del_dia_impl import ConsultarAsistenciasDelDiaImpl
from asistencia.application.use_cases.impl.consultar_asistencias_del_periodo_impl import ConsultarAsistenciasDelPeriodoImpl
from asistencia.application.use_cases.use_cases import (
    RegistrarAsistencia,
    BuscarAsistencias,
    ConsultarAsistenciasDelDia,
    ConsultarAsistenciasDelPeriodo,
)
from asistencia.domain.ports import AsistenciaRepository
from asistencia.infrastructure.repositories import AsistenciaRepositoryImpl


class AsistenciaInjectorModule(Module):
    @singleton
    @provider
    def provide_mapper(self) -> AsistenciaMapper:
        return AsistenciaMapperImpl()
    
    @singleton
    @provider
    def provide_asistencia_repository(self) -> AsistenciaRepository:
        return AsistenciaRepositoryImpl(self.provide_mapper())

    @singleton
    @provider
    def provide_registrar_asistencia(self) -> RegistrarAsistencia:
        return RegistrarAsistenciaImpl(
            repository=self.provide_asistencia_repository(),
            mapper=self.provide_mapper()
        )

    @singleton
    @provider
    def provide_buscar_asistencias(self,repo: AsistenciaRepository, mapper: AsistenciaMapper) -> BuscarAsistencias:
        return BuscarAsistenciasImpl(repository=repo, mapper=mapper)

    @singleton
    @provider
    def provide_consultar_por_dia(self) -> ConsultarAsistenciasDelDia:
        return ConsultarAsistenciasDelDiaImpl(
            repository=self.provide_asistencia_repository(),
            mapper=self.provide_mapper()
        )

    @singleton
    @provider
    def provide_consultar_por_periodo(self) -> ConsultarAsistenciasDelPeriodo:
        return ConsultarAsistenciasDelPeriodoImpl(
            repository=self.provide_asistencia_repository(),
            mapper=self.provide_mapper()
        )