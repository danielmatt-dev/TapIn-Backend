from alumnos.domain.models import Alumnos

class AlumnoRepositoryImpl:
    def registrar(self, data):
        return Alumnos.objects.create(**data)

    def obtener_por_correo(self, correo):
        return Alumnos.objects.filter(correo_institucional=correo).first()
