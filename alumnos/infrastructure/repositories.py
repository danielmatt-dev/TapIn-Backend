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
        model = self._mapper.to_model(alumno)
        model.save()
        return self._mapper.to_domain(model)

    def obtener_por_correo(self, correo: str) -> Alumno:
        return AlumnoModel.objects.filter(correo_institucional=correo).first()
    
    def obtener_por_id(self, id_alumno: str) -> Alumno:
        model = AlumnoModel.objects.filter(id_alumno=id_alumno).first()
        return self._mapper.to_domain(model) if model else None

    def actualizar(self, alumno: Alumno) -> None:
        model = AlumnoModel.objects.get(id_alumno=alumno.id_alumno)
        model.es_silenciado = alumno.es_silenciado
        model.save()
    
    def eliminar(self, id_alumno: str) -> bool:
        deleted, _ = AlumnoModel.objects.filter(id_alumno=id_alumno).delete()
        return bool(deleted)

    def obtener_todos(self) -> list:
        models = AlumnoModel.objects.all()
        return [self._mapper.to_domain(model) for model in models]