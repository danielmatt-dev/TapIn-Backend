# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alumnos(models.Model):
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
