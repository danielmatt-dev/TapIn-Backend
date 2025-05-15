from rest_framework import serializers
from bloques.infrastructure.serializers import BloqueSerializer

class PeriodoSerializer(serializers.Serializer):
    id_periodo   = serializers.CharField()
    nombre       = serializers.CharField()
    hora_entrada = serializers.TimeField()
    hora_salida  = serializers.TimeField()
    fecha_inicio = serializers.DateField()
    fecha_final  = serializers.DateField()
    estado       = serializers.ChoiceField(choices=['Habilitado','Deshabilitado'])
    bloques      = BloqueSerializer(many=True)   # <-- anidado
