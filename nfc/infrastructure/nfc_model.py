from django.db import models

class NFCModel(models.Model):
    id_nfc        = models.AutoField(primary_key=True)
    identificador = models.CharField(max_length=255)
    id_alumno     = models.CharField(max_length=255) 
    estado        = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'nfc'
        app_label = 'nfc'
