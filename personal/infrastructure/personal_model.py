from django.db import models

class PersonalModel(models.Model):
    id_personal = models.CharField(primary_key=True, max_length=255)
    nombre      = models.CharField(max_length=255)
    rol         = models.CharField(max_length=20)
    departamento= models.CharField(max_length=100)
    correo      = models.CharField(max_length=255)
    estado      = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'personal'
