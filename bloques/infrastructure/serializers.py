from rest_framework import serializers

class BloqueSerializer(serializers.Serializer):
    id_bloque  = serializers.CharField()
    id_periodo = serializers.CharField()
    nombre     = serializers.CharField()
    meses      = serializers.CharField()
    estado     = serializers.ChoiceField(choices=['Habilitado', 'Deshabilitado'])
