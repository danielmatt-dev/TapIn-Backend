from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from alumnos.application.use_cases.use_cases import RegistrarAlumno
from alumnos.domain.dtos import AlumnoDTO
from alumnos.infrastructure.serializers import AlumnoSerializer

@csrf_exempt
@api_view(['POST'])
def registrar_alumno_view(request, registrar_alumno: RegistrarAlumno):
    alumno_serializer = AlumnoSerializer(data=request.data)

    if not alumno_serializer.is_valid():
        return Response(alumno_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    alumno_request = AlumnoDTO(
        id_alumno=alumno_serializer.validated_data['id_alumno'],
        nombre_completo=alumno_serializer.validated_data['nombre_completo'],
        curp=alumno_serializer.validated_data['curp'],
        sexo=alumno_serializer.validated_data['sexo'],
        correo_institucional=alumno_serializer.validated_data['correo_institucional'],
        fecha_nacimiento=alumno_serializer.validated_data['fecha_nacimiento'],
        telefono_tutor=alumno_serializer.validated_data['telefono_tutor'],
    )

    alumno_response = registrar_alumno.execute(alumno_request)
    alumno_serializable = AlumnoSerializer(alumno_response).data

    return Response(alumno_serializable, status=status.HTTP_201_CREATED)
