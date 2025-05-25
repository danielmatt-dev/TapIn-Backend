from django.db import models


class AlertaModel(models.Model):
    id_alerta = models.CharField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=225)
    tipo = models.CharField()
    estado = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'alertas'
