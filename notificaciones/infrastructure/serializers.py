from rest_framework import serializers

class NotificacionRequestSerializer(serializers.Serializer):

    id_nfc           = serializers.IntegerField()
    id_notificacion  = serializers.IntegerField()

class AlertaRequestSerializer(serializers.Serializer):

    id_alumno        = serializers.CharField()
    id_notificacion  = serializers.IntegerField()
