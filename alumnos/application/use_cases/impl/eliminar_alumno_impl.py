from injector import inject

from alumnos.application.use_cases.use_cases import EliminarAlumno
from alumnos.domain.ports import AlumnoRepository

class EliminarAlumnoImpl(EliminarAlumno):

    @inject
    def __init__(self, repository: AlumnoRepository):
        self._repository = repository

    def execute(self, id_alumno: str) -> bool:
        return self._repository.eliminar(id_alumno)
