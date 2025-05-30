from injector import Module, singleton, provider, Injector

from alertas.domain.alerta_port import AlertaRepository
from alertas.infraestructure.alerta_repository import AlertaRepositoryImpl
from alumnos.domain.ports import AlumnoRepository
from alumnos.infrastructure.injector_modules import AlumnoInjectorModule
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
from inscripciones.domain.ports import InscripcionRepository
from inscripciones.infrastructure.injector_modules import InscripcionesInjectorModule
from nfc.domain.ports import NFCRepository
from nfc.infrastructure.injector_modules import NFCInjectorModule


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
    def provide_alerta_repository(self) -> AlertaRepository:
        return AlertaRepositoryImpl()

    @singleton
    @provider
    def provide_registrar_asistencia(self) -> RegistrarAsistencia:
        injector = Injector([NFCInjectorModule])
        alu_injector = Injector([AlumnoInjectorModule])

        return RegistrarAsistenciaImpl(
            repository=self.provide_asistencia_repository(),
            mapper=self.provide_mapper(),
            alerta_repository=self.provide_alerta_repository(),
            nfc_repository=injector.get(NFCRepository),
            alumno_repository=alu_injector.get(AlumnoRepository)
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
        injector = Injector([AlumnoInjectorModule])
        injector_ins = Injector([InscripcionesInjectorModule])

        return ConsultarAsistenciasDelPeriodoImpl(
            repository=self.provide_asistencia_repository(),
            alumno_repository=injector.get(AlumnoRepository),
            inscripcion_repository=injector_ins.get(InscripcionRepository)
        )
