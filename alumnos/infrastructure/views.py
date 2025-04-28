from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from alumnos.application.use_cases.use_cases import RegistrarAlumno, SilenciarAlumno, EliminarAlumno, ConsultarEstadoAlumnos
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


@csrf_exempt
@api_view(['POST'])
def silenciar_alumno_view(request, silenciar_alumno: SilenciarAlumno):
    id_alumno = request.data.get('id_alumno')

    if not id_alumno:
        return Response({"error": "id_alumno es requerido"}, status=status.HTTP_400_BAD_REQUEST)

    success = silenciar_alumno.execute(id_alumno)
    return Response({"success": success}, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['DELETE'])
def eliminar_alumno_view(request, eliminar_alumno: EliminarAlumno):
    id_alumno = request.data.get('id_alumno')

    if not id_alumno:
        return Response({"error": "id_alumno es requerido"}, status=status.HTTP_400_BAD_REQUEST)

    success = eliminar_alumno.execute(id_alumno)
    return Response({"success": success}, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
def consultar_estado_alumnos_view(request, consultar_estado_alumnos: ConsultarEstadoAlumnos):
    alumnos = consultar_estado_alumnos.execute()
    alumnos_data = [a.__dict__ for a in alumnos]

    return Response(alumnos_data, status=status.HTTP_200_OK)
