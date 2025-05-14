from rest_framework import serializers

class PersonalSerializer(serializers.Serializer):
    id_personal = serializers.CharField()
    nombre      = serializers.CharField()
    rol         = serializers.ChoiceField(choices=['Administrativo','Directivo'])
    departamento= serializers.CharField()
    correo      = serializers.EmailField()
    estado      = serializers.ChoiceField(choices=['Habilitado','Deshabilitado'])
