from injector import inject

from alumnos.application.use_cases.use_cases import RegistrarAlumno
from alumnos.domain.alumno import Alumno
from alumnos.domain.ports import AlumnoRepository


class RegistrarAlumnoImpl(RegistrarAlumno):

    @inject
    def __init__(self, repository: AlumnoRepository):
        self._repository = repository

    def execute(self, dto: any) -> Alumno:
        alumno = Alumno('Daniel')
        return self._repository.registrar(alumno)
