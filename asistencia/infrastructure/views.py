from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from asistencia.application.use_cases.use_cases import (
    RegistrarAsistencia,
    BuscarAsistencias,
    ConsultarAsistenciasDelDia,
    ConsultarAsistenciasDelPeriodo
)
from asistencia.domain.dtos import AsistenciaDTO
from asistencia.infrastructure.serializers import AsistenciaSerializer

@csrf_exempt
@api_view(['POST'])
def registrar_asistencia_view(request, use_case: RegistrarAsistencia):
    ser = AsistenciaSerializer(data=request.data)
    if not ser.is_valid():
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    dto = AsistenciaDTO.nuevo(
        id_alumno=ser.validated_data['id_alumno'],
        fecha=ser.validated_data['fecha'],
        hora=ser.validated_data['hora'],
        tipo_registro=ser.validated_data['tipo_registro'],
        tipo_acceso=ser.validated_data['tipo_acceso'],
        estado=ser.validated_data['estado'],
    )
    creado = use_case.execute(dto)
    return Response(AsistenciaSerializer(creado).data, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['GET'])
def buscar_asistencias_view(request, buscar_uc: BuscarAsistencias):
    id_alumno = request.query_params.get('id_alumno')
    if not id_alumno:
        return Response({"error": "id_alumno es requerido"}, status=status.HTTP_400_BAD_REQUEST)

    dtos = buscar_uc.execute(id_alumno)
    serializer = AsistenciaSerializer(dtos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def consultar_por_dia_view(request, use_case: ConsultarAsistenciasDelDia):
    from datetime import datetime
    qs = request.query_params.get('fecha')
    try:
        fecha = datetime.fromisoformat(qs).date()
    except:
        return Response({"error":"fecha inválida"}, status=status.HTTP_400_BAD_REQUEST)
    regs = use_case.execute(fecha)
    return Response(AsistenciaSerializer(regs, many=True).data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def consultar_por_periodo_view(request, use_case: ConsultarAsistenciasDelPeriodo):
    from datetime import datetime
    fi = request.query_params.get('fecha_inicio')
    ff = request.query_params.get('fecha_fin')
    try:
        inicio = datetime.fromisoformat(fi).date()
        fin    = datetime.fromisoformat(ff).date()
    except:
        return Response({"error":"fechas inválidas"}, status=status.HTTP_400_BAD_REQUEST)
    regs = use_case.execute(inicio, fin)
    return Response(AsistenciaSerializer(regs, many=True).data, status=status.HTTP_200_OK)
