from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from inscripciones.application.use_cases.use_cases import (
    NuevaInscripcion, BuscarInscripciones,
    ActualizarPeriodo, VaciarInscripciones
)
from inscripciones.domain.dtos import InscripcionDTO
from inscripciones.infrastructure.serializers import InscripcionSerializer

@csrf_exempt
@api_view(['POST'])
def registrar_inscripcion_view(request, uc: NuevaInscripcion):
    ser = InscripcionSerializer(data=request.data)
    if not ser.is_valid():
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    dto = InscripcionDTO.nuevo(
        id_alumno=ser.validated_data['id_alumno'],
        id_periodo=ser.validated_data['id_periodo'],
        fecha=ser.validated_data['fecha'],
        grado=ser.validated_data.get('grado', ''),
        grupo=ser.validated_data.get('grupo', ''),
        estado=ser.validated_data['estado'],
    )
    creado = uc.execute(dto)
    return Response(InscripcionSerializer(creado).data, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['GET'])
def buscar_inscripciones_view(request, uc: BuscarInscripciones):
    id_alumno = request.query_params.get('id_alumno')
    if not id_alumno:
        return Response({"error":"id_alumno es requerido"}, status=status.HTTP_400_BAD_REQUEST)
    dtos = uc.execute(id_alumno)
    return Response(InscripcionSerializer(dtos, many=True).data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['PATCH'])
def actualizar_periodo_view(request, uc: ActualizarPeriodo):
    id_ins = request.data.get('id_inscripcion')
    nuevo  = request.data.get('id_periodo')
    if not id_ins or not nuevo:
        return Response({"error":"id_inscripcion e id_periodo requeridos"}, status=status.HTTP_400_BAD_REQUEST)
    ok = uc.execute(id_ins, nuevo)
    return Response({"success": ok}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['DELETE'])
def vaciar_inscripciones_view(request, uc: VaciarInscripciones):
    id_periodo = request.data.get('id_periodo')
    if not id_periodo:
        return Response({"error":"id_periodo es requerido"}, status=status.HTTP_400_BAD_REQUEST)
    count = uc.execute(id_periodo)
    return Response({"deleted": count}, status=status.HTTP_200_OK)
