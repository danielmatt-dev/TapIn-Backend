from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from inscripciones.application.use_cases.use_cases import (
    NuevaInscripcion, BuscarInscripciones, ActualizarPeriodo, VaciarInscripciones
)
from inscripciones.domain.dtos import InscripcionDTO
from inscripciones.infrastructure.serializers import InscripcionSerializer

@csrf_exempt
@api_view(['POST'])
def registrar_inscripcion_view(request, use_case: NuevaInscripcion):
    ser = InscripcionSerializer(data=request.data)
    if not ser.is_valid():
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    dto = InscripcionDTO(
        id_inscripcion=ser.validated_data['id_inscripcion'],
        id_alumno=ser.validated_data['id_alumno'],
        id_periodo=ser.validated_data['id_periodo'],
        fecha=ser.validated_data['fecha'],
        grado=ser.validated_data.get('grado', ''),
        grupo=ser.validated_data.get('grupo', ''),
        estado=ser.validated_data['estado']
    )
    creado = use_case.execute(dto)
    return Response(InscripcionSerializer(creado).data, status=status.HTTP_201_CREATED)

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
    id_inscripcion = request.data.get('id_inscripcion')
    id_periodo     = request.data.get('id_periodo')
    if not id_inscripcion or not id_periodo:
        return Response(
            {"error": "id_inscripcion e id_periodo son requeridos"},
            status=status.HTTP_400_BAD_REQUEST
        )
    success = use_case.execute(id_inscripcion, id_periodo)
    return Response({"success": success}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['DELETE'])
def vaciar_inscripciones_view(request, use_case: VaciarInscripciones):
    success = use_case.execute()
    return Response({"success": success}, status=status.HTTP_200_OK)
