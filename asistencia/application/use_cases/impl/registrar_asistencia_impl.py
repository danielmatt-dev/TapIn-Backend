from injector import inject
from rest_framework.exceptions import NotFound

from alertas.domain.alerta_port import AlertaRepository
from alumnos.domain.ports import AlumnoRepository
from asistencia.application.use_cases.use_cases import RegistrarAsistencia
from asistencia.domain.dtos import AsistenciaDTO
from asistencia.domain.asistencia import Asistencia
from asistencia.domain.ports import AsistenciaRepository
from asistencia.infrastructure.mapper.asistencia_mapper import AsistenciaMapper
from nfc.domain.ports import NFCRepository


class RegistrarAsistenciaImpl(RegistrarAsistencia):

    @inject
    def __init__(self,
                 repository: AsistenciaRepository,
                 nfc_repository: NFCRepository,
                 alerta_repository: AlertaRepository,
                 alumno_repository: AlumnoRepository,
                 mapper: AsistenciaMapper):
        self._repo = repository
        self._mapper = mapper
        self._nfc_repository = nfc_repository
        self._alerta_repository = alerta_repository
        self._alumno_repository = alumno_repository

    def execute(self, dto: AsistenciaDTO) -> AsistenciaDTO:
        # 1) Buscar alumno por correo, si viene en el DTO
        if dto.correo:
            alumno = self._alumno_repository.obtener_por_correo(dto.correo)
            if alumno is None:
                raise NotFound("Alumno no encontrado para el correo proporcionado")
        else:
            # 2) Si no hay correo, buscar por NFC
            nfc = self._nfc_repository.obtener_por_id(dto.id_nfc)
            if nfc is None:
                raise NotFound("NFC no encontrado")
            alumno = nfc.alumno

        # 3) Buscar alerta (y validar que exista)
        alerta = self._alerta_repository.buscar_por_id(id_alerta=1)
        if alerta is None:
            raise NotFound("Alerta no encontrada")

        # 4) Formatear mensaje de alerta
        params = {
            "studentName": alumno.nombre_completo,
            "time": dto.hora,
        }
        mensaje = alerta.descripcion.format(**params)
        print(mensaje)

        # 5) Registrar asistencia
        entidad = Asistencia(
            id_registro_asistencia=None,
            id_alumno=alumno.id_alumno,
            fecha=dto.fecha,
            hora=dto.hora,
            tipo_registro=dto.tipo_registro,
            tipo_acceso=dto.tipo_acceso,
            estado='Habilitado',
        )
        creado = self._repo.registrar(entidad)

        return self._mapper.to_dto(creado, alumno.correo_institucional)
