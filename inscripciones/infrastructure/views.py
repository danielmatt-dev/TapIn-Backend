from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from inscripciones.application.use_cases.use_cases import (
    NuevaInscripcion, BuscarInscripciones, ActualizarPeriodo, ObtenerDatos
)
from inscripciones.domain.dtos import InscripcionDTO
from inscripciones.infrastructure.serializers import InscripcionSerializer
from inscripciones.infrastructure.serializers_dto import DatosCompletosSerializer

from periodos.infrastructure.repositories import PeriodoRepositoryImpl
from alumnos.infrastructure.mapper.alumno_mapper_impl import AlumnoMapperImpl
from periodos.infrastructure.mapper.periodo_mapper_impl import PeriodoMapperImpl
from inscripciones.infrastructure.serializers import ActualizarPeriodoSerializer



@csrf_exempt
@api_view(['POST'])
def registrar_inscripcion_view(request, use_case: NuevaInscripcion):
    ser = InscripcionSerializer(data=request.data)
    ser.is_valid(raise_exception=True)

    alumno_model  = ser.validated_data.pop('alumno')
    periodo_model = ser.validated_data.pop('periodo')

    alumno  = AlumnoMapperImpl().to_domain(alumno_model)
    periodo = PeriodoMapperImpl().to_domain(periodo_model)

    dto = InscripcionDTO.nuevo(
        id_inscripcion=ser.validated_data['id_inscripcion'],
        alumno=alumno,
        periodo=periodo,
        fecha=ser.validated_data['fecha'],
        grado=ser.validated_data.get('grado',''),
        grupo=ser.validated_data.get('grupo',''),
        estado=ser.validated_data['estado']
    )

    model_guardado = use_case.execute(dto)

    return Response(InscripcionSerializer(model_guardado).data,
                    status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET'])
def buscar_inscripciones_view(request, use_case: BuscarInscripciones):
    id_alumno = request.query_params.get('id_alumno')
    if not id_alumno:
        return Response({"error": "id_alumno es requerido"}, status=status.HTTP_400_BAD_REQUEST)
    dtos = use_case.execute(id_alumno)
    return Response(InscripcionSerializer(dtos, many=True).data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['PUT'])
def actualizar_periodo_view(request, use_case: ActualizarPeriodo):
    ser = ActualizarPeriodoSerializer(data=request.data)
    ser.is_valid(raise_exception=True)

    id_insc  = ser.validated_data['id_inscripcion']
    periodo_model = ser.validated_data['periodo']

    periodo = PeriodoMapperImpl().to_domain(periodo_model)

    success = use_case.execute(id_insc, periodo)
    if not success:
        return Response(
            {"error": "No se encontró la inscripción o no se actualizó."},
            status=status.HTTP_400_BAD_REQUEST
        )
    return Response({"success": True}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def obtener_datos_view(request, use_case: ObtenerDatos):
    datos_dto = use_case.execute()
    ser       = DatosCompletosSerializer(datos_dto)
    return Response(ser.data, status=status.HTTP_200_OK)
