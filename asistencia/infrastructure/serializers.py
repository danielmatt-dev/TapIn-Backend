from rest_framework import serializers

class AsistenciaSerializer(serializers.Serializer):
    id_registro_asistencia = serializers.IntegerField(read_only=True)
    id_alumno              = serializers.CharField()
    fecha                  = serializers.DateField()
    hora                   = serializers.TimeField()
    tipo_registro          = serializers.ChoiceField(choices=['Normal','Justificada','Extraordinario','Tardío'])
    tipo_acceso            = serializers.ChoiceField(choices=['Entrada','Salida'])
    estado                 = serializers.ChoiceField(choices=['Habilitado','Deshabilitado'])
