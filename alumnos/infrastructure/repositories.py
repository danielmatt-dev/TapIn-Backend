from alumnos.domain.models import Alumnos
from alumnos.domain.ports import AlumnoRepository

class AlumnoRepositoryImpl(AlumnoRepository):
    def registrar(self, data: dict) -> Alumnos:
        return Alumnos.objects.create(**data)

    def obtener_por_correo(self, correo: str) -> Alumnos | None:
        return Alumnos.objects.filter(correo_institucional=correo).first()
