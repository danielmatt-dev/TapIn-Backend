from django.db import models

class InscripcionModel(models.Model):
    id_inscripcion = models.CharField(primary_key=True, max_length=255)
    id_alumno      = models.CharField(max_length=255)
    id_periodo     = models.CharField(max_length=255)
    fecha          = models.DateTimeField()
    grado          = models.CharField(max_length=5, blank=True, null=True)
    grupo          = models.CharField(max_length=5, blank=True, null=True)
    estado         = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'inscripciones'
