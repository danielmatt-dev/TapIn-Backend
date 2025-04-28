from injector import inject

from alumnos.application.use_cases.use_cases import SilenciarAlumno
from alumnos.domain.ports import AlumnoRepository

class SilenciarAlumnoImpl(SilenciarAlumno):

    @inject
    def __init__(self, repository: AlumnoRepository):
        self._repository = repository

    def execute(self, id_alumno: str) -> bool:
        alumno = self._repository.obtener_por_id(id_alumno)
        if alumno:
            alumno.es_silenciado = True
            self._repository.actualizar(alumno)
            return True
        return False
