from injector import inject

from alumnos.application.use_cases.use_cases import SilenciarAlumno
from alumnos.domain.ports import AlumnoRepository

class SilenciarAlumnoImpl(SilenciarAlumno):

    @inject
    def __init__(self, repository: AlumnoRepository):
        self._repository = repository

    def execute(self, id_alumno: str, silenciado: bool) -> bool:
        return self._repository.silenciar(id_alumno, silenciado)
