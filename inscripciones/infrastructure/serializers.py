from rest_framework import serializers

class InscripcionSerializer(serializers.Serializer):
    id_inscripcion = serializers.CharField()
    id_alumno      = serializers.CharField()
    id_periodo     = serializers.CharField()
    fecha          = serializers.DateTimeField()
    grado          = serializers.CharField(allow_blank=True, required=False)
    grupo          = serializers.CharField(allow_blank=True, required=False)
    estado         = serializers.ChoiceField(choices=['Activo','Baja'])
