from django.views.decorators.csrf import csrf_exempt
from oauth2_provider.decorators import protected_resource
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from alumnos.application.use_cases.use_cases import RegistrarAlumno, SilenciarAlumno, EliminarAlumno, ConsultarEstadoAlumnos, ActualizarAlumno
from alumnos.domain.dtos import AlumnoDTO
from alumnos.infrastructure.serializers import AlumnoSerializer


@csrf_exempt
@api_view(['POST'])
@protected_resource()
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
        es_silenciado=alumno_serializer.validated_data.get('es_silenciado', False),
        estado=alumno_serializer.validated_data['estado']
    )

    alumno_response = registrar_alumno.execute(alumno_request)
    alumno_serializable = AlumnoSerializer(alumno_response).data

    return Response(alumno_serializable, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['POST'])
def silenciar_alumno_view(request, silenciar_alumno: SilenciarAlumno):
    id_alumno  = request.data.get('id_alumno')
    silenciado = request.data.get('silenciado')

    if id_alumno is None or silenciado is None:
        return Response(
            {"error": "Los campos 'id_alumno' y 'silenciado' son requeridos"},
            status=status.HTTP_400_BAD_REQUEST
        )

    success = silenciar_alumno.execute(id_alumno, silenciado)
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
    serializer = AlumnoSerializer(alumnos, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['PUT'])
def actualizar_alumno_view(request, actualizar_alumno: ActualizarAlumno):
    serializer = AlumnoSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    dto = AlumnoDTO(
        id_alumno=serializer.validated_data['id_alumno'],
        nombre_completo=serializer.validated_data['nombre_completo'],
        curp=serializer.validated_data['curp'],
        sexo=serializer.validated_data['sexo'],
        correo_institucional=serializer.validated_data['correo_institucional'],
        fecha_nacimiento=serializer.validated_data['fecha_nacimiento'],
        telefono_tutor=serializer.validated_data['telefono_tutor'],
        es_silenciado=serializer.validated_data.get('es_silenciado', False),
        estado=serializer.validated_data.get('estado', 'Activo'),
    )
    updated = actualizar_alumno.execute(dto)
    return Response(AlumnoSerializer(updated).data, status=status.HTTP_200_OK)