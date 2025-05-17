from django.db import models

class NotificacionModel(models.Model):
    id_alerta   = models.AutoField(primary_key=True)
    titulo      = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    tipo        = models.CharField(max_length=20)   # 'Alerta' | 'Notificación'
    estado      = models.CharField(max_length=15)   # 'Habilitado' | 'Deshabilitado'

    class Meta:
        db_table = 'alertas'
        managed  = False
