from rest_framework import serializers

class AlumnoDTOSerializer(serializers.Serializer):
    id_alumno            = serializers.CharField()
    nombre_completo      = serializers.CharField()
    curp                 = serializers.CharField()
    sexo                 = serializers.CharField()
    correo_institucional = serializers.EmailField()
    fecha_nacimiento     = serializers.DateField()
    telefono_tutor       = serializers.CharField()
    es_silenciado        = serializers.BooleanField()
    estado               = serializers.CharField()

class BloqueDTOSerializer(serializers.Serializer):
    id_bloque   = serializers.CharField()
    nombre      = serializers.CharField()
    hora_inicio = serializers.TimeField()
    hora_fin    = serializers.TimeField()

class PeriodoDTOSerializer(serializers.Serializer):
    id_periodo   = serializers.CharField()
    nombre       = serializers.CharField()
    hora_entrada = serializers.TimeField()
    hora_salida  = serializers.TimeField()
    fecha_inicio = serializers.DateField()
    fecha_final  = serializers.DateField()
    estado       = serializers.CharField()
    bloques      = BloqueDTOSerializer(many=True)

class InscripcionDTOSerializer(serializers.Serializer):
    id_inscripcion = serializers.CharField()
    alumno         = AlumnoDTOSerializer()
    periodo        = PeriodoDTOSerializer()
    fecha          = serializers.DateTimeField()
    grado          = serializers.CharField(allow_blank=True, required=False)
    grupo          = serializers.CharField(allow_blank=True, required=False)
    estado         = serializers.CharField()

class DatosCompletosSerializer(serializers.Serializer):
    alumnos       = AlumnoDTOSerializer(many=True)
    inscripciones = InscripcionDTOSerializer(many=True)
    periodos      = PeriodoDTOSerializer(many=True)
