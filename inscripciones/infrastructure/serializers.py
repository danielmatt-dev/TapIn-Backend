from rest_framework import serializers
from inscripciones.infrastructure.inscripcion_model import InscripcionModel
from alumnos.infrastructure.alumno_model import AlumnoModel
from periodos.infrastructure.periodo_model import PeriodoModel

class InscripcionSerializer(serializers.ModelSerializer):
    alumno  = serializers.PrimaryKeyRelatedField(queryset=AlumnoModel.objects.all())
    periodo = serializers.PrimaryKeyRelatedField(queryset=PeriodoModel.objects.all())

    class Meta:
        model  = InscripcionModel
        fields = [
            'id_inscripcion',
            'alumno',
            'periodo',
            'fecha',
            'grado',
            'grupo',
            'estado',
        ]

class ActualizarPeriodoSerializer(serializers.Serializer):
    id_inscripcion = serializers.CharField()
    periodo        = serializers.PrimaryKeyRelatedField(queryset=PeriodoModel.objects.all())
