from injector import inject
from typing import List

from alumnos.application.use_cases.use_cases import ConsultarEstadoAlumnos
from alumnos.domain.dtos import AlumnoDTO, AlumnoResponseDTO
from alumnos.domain.ports import AlumnoRepository
from alumnos.infrastructure.mapper.alumno_mapper import AlumnoMapper
from nfc.domain.ports import NFCRepository


class ConsultarEstadoAlumnosImpl(ConsultarEstadoAlumnos):

    @inject
    def __init__(self,
                 repository: AlumnoRepository,
                 nfc_repository: NFCRepository,
                 mapper: AlumnoMapper):
        self._repository = repository
        self._mapper = mapper
        self._nfc_repository = nfc_repository

    def execute(self) -> List[AlumnoResponseDTO]:
        alumnos = self._repository.obtener_todos()
        dtos = []
        for alumno in alumnos:
            nfc = self._nfc_repository.obtener_por_id_alumno(alumno.id_alumno)
            if not nfc:
                continue

            response = AlumnoResponseDTO(
                id_nfc=nfc.identificador,
                nombre_completo=alumno.nombre_completo,
                correo_institucional=alumno.correo_institucional,
                estado=alumno.estado
            )
            dtos.append(response)

        return dtos
