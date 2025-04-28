from injector import inject
from typing import List

from alumnos.application.use_cases.use_cases import ConsultarEstadoAlumnos
from alumnos.domain.dtos import AlumnoDTO
from alumnos.domain.ports import AlumnoRepository
from alumnos.infrastructure.mapper.alumno_mapper import AlumnoMapper

class ConsultarEstadoAlumnosImpl(ConsultarEstadoAlumnos):

    @inject
    def __init__(self, repository: AlumnoRepository, mapper: AlumnoMapper):
        self._repository = repository
        self._mapper = mapper

    def execute(self) -> List[AlumnoDTO]:
        alumnos = self._repository.obtener_todos()
        return [self._mapper.to_dto(a) for a in alumnos]
