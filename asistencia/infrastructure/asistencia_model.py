from django.db import models

class AsistenciaModel(models.Model):
    id_registro_asistencia = models.AutoField(primary_key=True)
    id_alumno              = models.CharField(max_length=255)
    fecha                  = models.DateField()
    hora                   = models.TimeField()
    tipo_registro          = models.CharField(max_length=20)
    tipo_acceso            = models.CharField(max_length=10)
    estado                 = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'registro_asistencias'
