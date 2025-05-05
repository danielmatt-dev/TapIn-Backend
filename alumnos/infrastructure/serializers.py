from rest_framework import serializers


class AlumnoSerializer(serializers.Serializer):
    id_alumno = serializers.CharField()
    nombre_completo = serializers.CharField()
    curp = serializers.CharField()
    sexo = serializers.CharField()
    correo_institucional = serializers.EmailField()
    fecha_nacimiento = serializers.DateField()
    telefono_tutor = serializers.CharField()
    es_silenciado = serializers.BooleanField(read_only=True)
    estado = serializers.ChoiceField(choices=['Activo','Baja'])  
