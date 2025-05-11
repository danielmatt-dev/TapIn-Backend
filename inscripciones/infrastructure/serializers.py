from rest_framework import serializers

class InscripcionSerializer(serializers.Serializer):
    id_inscripcion = serializers.CharField(required=False)
    id_alumno      = serializers.CharField()
    id_periodo     = serializers.CharField()
    fecha          = serializers.DateTimeField()
    grado          = serializers.CharField(required=False, allow_blank=True)
    grupo          = serializers.CharField(required=False, allow_blank=True)
    estado         = serializers.ChoiceField(choices=['Activo','Baja'])
