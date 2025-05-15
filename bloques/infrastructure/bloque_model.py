from django.db import models

class BloqueModel(models.Model):
    id_bloque   = models.CharField(primary_key=True, max_length=255)
    id_periodo  = models.CharField(max_length=255)
    nombre      = models.CharField(max_length=100)
    meses       = models.CharField(max_length=50)
    estado      = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'bloques'
