from rest_framework import serializers

class AsistenciaSerializer(serializers.Serializer):
    id_registro_asistencia = serializers.IntegerField(read_only=True)
    id_nfc              = serializers.CharField()
    fecha                  = serializers.DateField()
    hora                   = serializers.TimeField()
    tipo_registro          = serializers.ChoiceField(choices=['Normal','Justificada','Extraordinario','Tardío'])
    tipo_acceso            = serializers.ChoiceField(choices=['Entrada','Salida'])
    estado                 = serializers.ChoiceField(choices=['Habilitado','Deshabilitado'])


class AsistenciaResponseSerializer(serializers.Serializer):
    id_registro_asistencia = serializers.IntegerField(allow_null=True, read_only=True)
    alumno                  = serializers.CharField()
    correo                  = serializers.EmailField()
    grado                   = serializers.CharField()
    grupo                   = serializers.CharField()
    fecha                   = serializers.DateField()
    hora                    = serializers.TimeField()
    tipo_registro           = serializers.ChoiceField(
                                  choices=['Normal', 'Justificada', 'Extraordinario', 'Tardío']
                               )
    tipo_acceso             = serializers.ChoiceField(
                                  choices=['Entrada', 'Salida']
                               )
    estado                  = serializers.ChoiceField(
                                  choices=['Habilitado', 'Deshabilitado']
                               )