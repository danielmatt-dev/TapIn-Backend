from injector import inject
from datetime import date
from typing import List

from alumnos.domain.ports import AlumnoRepository
from asistencia.application.use_cases.use_cases import ConsultarAsistenciasDelPeriodo
from asistencia.domain.dtos import AsistenciaResponse
from asistencia.domain.ports import AsistenciaRepository


class ConsultarAsistenciasDelPeriodoImpl(ConsultarAsistenciasDelPeriodo):

    @inject
    def __init__(self,
                 repository: AsistenciaRepository,
                 alumno_repository: AlumnoRepository):

        self._repo = repository
        self._alumno_repository = alumno_repository

    def execute(self, fecha_inicio: date, fecha_fin: date) -> List[AsistenciaResponse]:
        regs = self._repo.consultar_por_periodo(fecha_inicio, fecha_fin)

        asistencias_response = []
        for r in regs:
            alumno = self._alumno_repository.obtener_por_id(r.id_alumno)
            asistencia = AsistenciaResponse(
                id_registro_asistencia=r.id_registro_asistencia,
                fecha=r.fecha,
                hora=r.hora,
                tipo_registro=r.tipo_registro,
                tipo_acceso=r.tipo_acceso,
                estado=r.estado,
                alumno=alumno.nombre_completo,
            )
            asistencias_response.append(asistencia)

        return asistencias_response
