from django.db import models


class AlumnoModel(models.Model):
    id_alumno = models.CharField(primary_key=True)
    nombre_completo = models.CharField()
    curp = models.CharField(max_length=50)
    sexo = models.CharField(max_length=20)
    correo_institucional = models.CharField()
    fecha_nacimiento = models.DateField()
    telefono_tutor = models.CharField(blank=True, null=True)
    es_silenciado = models.BooleanField()
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'alumnos'
