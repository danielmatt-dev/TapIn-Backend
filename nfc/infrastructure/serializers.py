from rest_framework import serializers
from alumnos.infrastructure.serializers import AlumnoSerializer

class NFCOutputSerializer(serializers.Serializer):
    id_nfc        = serializers.IntegerField(read_only=True)
    identificador = serializers.CharField()
    alumno        = AlumnoSerializer()   
    estado        = serializers.ChoiceField(choices=['Habilitado','Deshabilitado'])
