from django.db import models

class PeriodoModel(models.Model):
    id_periodo  = models.CharField(primary_key=True)
    nombre      = models.CharField()
    hora_entrada= models.TimeField()
    hora_salida = models.TimeField()
    fecha_inicio= models.DateField()
    fecha_final = models.DateField()
    estado      = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'periodos'
        app_label = 'periodos'
