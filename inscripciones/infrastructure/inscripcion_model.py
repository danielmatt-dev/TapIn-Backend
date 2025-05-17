from django.db import models
from alumnos.infrastructure.alumno_model import AlumnoModel
from periodos.infrastructure.periodo_model import PeriodoModel

class InscripcionModel(models.Model):
    id_inscripcion = models.CharField(primary_key=True, max_length=255)
    alumno  = models.ForeignKey(AlumnoModel,
                                db_column='id_alumno',
                                on_delete=models.CASCADE)
    periodo = models.ForeignKey(PeriodoModel,
                                db_column='id_periodo',
                                on_delete=models.CASCADE)
    fecha   = models.DateTimeField()
    grado   = models.CharField(max_length=5, blank=True, null=True)
    grupo   = models.CharField(max_length=5, blank=True, null=True)
    estado  = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'inscripciones'
