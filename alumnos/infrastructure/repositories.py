from injector import inject

from alumnos.domain.alumno import Alumno
from alumnos.infrastructure.alumno_model import AlumnoModel
from alumnos.domain.ports import AlumnoRepository
from alumnos.infrastructure.mapper.alumno_mapper import AlumnoMapper


class AlumnoRepositoryImpl(AlumnoRepository):

    @inject
    def __init__(self, mapper: AlumnoMapper):
        self._mapper = mapper

    def registrar(self, alumno: Alumno) -> Alumno:
        model = self._mapper.toModel(alumno)
        return self._mapper.toDomain(AlumnoModel.objects.create(model))

    def obtener_por_correo(self, correo: str) -> Alumno:
        return AlumnoModel.objects.filter(correo_institucional=correo).first()
