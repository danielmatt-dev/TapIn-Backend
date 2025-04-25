from rest_framework import serializers
from alumnos.infrastructure.alumno_model import AlumnoModel

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumnoModel
        fields = '__all__'
