from dataclasses import dataclass
from rest_framework import serializers


@dataclass
class Alerta:
    id_alerta: int
    titulo: str
    descripcion: str
    tipo: str


class AlertaSerializer(serializers.Serializer):
    id_alerta    = serializers.IntegerField()
    titulo       = serializers.CharField()
    descripcion  = serializers.CharField()
    tipo         = serializers.CharField()