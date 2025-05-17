from injector import Module, singleton, provider
from notificaciones.domain.ports import NotificacionesRepository, SMSGateway
from notificaciones.infrastructure.mapper.notificacion_mapper import NotificacionMapper
from notificaciones.infrastructure.mapper.notificacion_mapper_impl import NotificacionMapperImpl
from notificaciones.infrastructure.repositories import NotificacionesRepositoryImpl
from notificaciones.application.use_cases.use_cases import EnviarNotificacion, EnviarAlerta
from notificaciones.application.use_cases.impl.enviar_notificacion_impl import EnviarNotificacionImpl
from notificaciones.application.use_cases.impl.enviar_alerta_impl import EnviarAlertaImpl
from alumnos.domain.ports import AlumnoRepository
from nfc.domain.ports import NFCRepository

class NotificacionesInjectorModule(Module):
    @singleton
    @provider
    def provide_notificacion_mapper(self) -> NotificacionMapper:
        return NotificacionMapperImpl()

    @singleton
    @provider
    def provide_notificaciones_repo(self, mapper: NotificacionMapper) -> NotificacionesRepository:
        return NotificacionesRepositoryImpl(mapper)

    @singleton
    @provider
    def provide_sms_gateway(self) -> SMSGateway:
        # Implementación por consola; aquí podrías inyectar Twilio, Nexmo, etc.
        class ConsoleSMSService(SMSGateway):
            def send_sms(self, telefono: str, mensaje: str) -> bool:
                print(f"Enviando SMS a {telefono}: {mensaje}")
                return True
        return ConsoleSMSService()

    @singleton
    @provider
    def provide_enviar_notificacion(
        self,
        nfc_repo: NFCRepository,
        repo: NotificacionesRepository,
        sms: SMSGateway
    ) -> EnviarNotificacion:
        return EnviarNotificacionImpl(nfc_repo, repo, sms)

    @singleton
    @provider
    def provide_enviar_alerta(
        self,
        alumno_repo: AlumnoRepository,
        repo: NotificacionesRepository,
        sms: SMSGateway
    ) -> EnviarAlerta:
        return EnviarAlertaImpl(alumno_repo, repo, sms)
