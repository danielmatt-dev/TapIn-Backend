from injector import Module, singleton, provider

from nfc.application.use_cases.impl.registrar_nfc_impl import RegistrarNFCImpl
from nfc.application.use_cases.impl.eliminar_nfc_impl import EliminarNFCImpl
from nfc.application.use_cases.impl.listar_nfc_impl import ListarNFCImpl
from nfc.application.use_cases.impl.actuallizar_estado_nfc_impl import ActualizarEstadoNFCImpl

from nfc.domain.ports import NFCRepository
from nfc.infrastructure.mapper.nfc_mapper import NFCMapper
from nfc.infrastructure.mapper.nfc_mapper_impl import NFCMapperImpl
from nfc.infrastructure.repositories import NFCRepositoryImpl

from alumnos.infrastructure.mapper.alumno_mapper_impl import AlumnoMapperImpl
from alumnos.domain.ports import AlumnoRepository
from alumnos.infrastructure.repositories import AlumnoRepositoryImpl

from nfc.application.use_cases.use_cases import (
    RegistrarNFC, EliminarNFC,
    ListarNFC, ActualizarEstadoNFC
)

class NFCInjectorModule(Module):

    @singleton
    @provider
    def provide_nfc_mapper(self) -> NFCMapper:
        return NFCMapperImpl()

    @singleton
    @provider
    def provide_alumno_mapper(self) -> AlumnoMapperImpl:
        return AlumnoMapperImpl()

    @singleton
    @provider
    def provide_alumno_repo(self) -> AlumnoRepository:
        return AlumnoRepositoryImpl(self.provide_alumno_mapper())

    @singleton
    @provider
    def provide_nfc_repo(self) -> NFCRepository:
        return NFCRepositoryImpl(
            mapper=self.provide_nfc_mapper(),
            alumno_repo=self.provide_alumno_repo()
        )

    @singleton
    @provider
    def provide_registrar(self) -> RegistrarNFC:
        return RegistrarNFCImpl(repo=self.provide_nfc_repo())

    @singleton
    @provider
    def provide_eliminar(self) -> EliminarNFC:
        return EliminarNFCImpl(repo=self.provide_nfc_repo())

    @singleton
    @provider
    def provide_listar(self) -> ListarNFC:
        return ListarNFCImpl(repo=self.provide_nfc_repo())

    @singleton
    @provider
    def provide_actualizar_estado(self) -> ActualizarEstadoNFC:
        return ActualizarEstadoNFCImpl(repo=self.provide_nfc_repo())
