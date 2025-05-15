from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from periodos.application.use_cases.use_cases import ConsultarPeriodo
from periodos.application.use_cases.use_cases import RegistrarPeriodo, BuscarPeriodos, EliminarPeriodo
from periodos.domain.dtos import PeriodoDTO
from periodos.infrastructure.serializers import PeriodoSerializer


@csrf_exempt
@api_view(['POST'])
def registrar_periodo_view(request, uc: RegistrarPeriodo):
    ser = PeriodoSerializer(data=request.data)
    if not ser.is_valid():
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    dto = PeriodoDTO(**ser.validated_data)
    creado = uc.execute(dto)
    return Response(PeriodoSerializer(creado).data, status=status.HTTP_201_CREATED)


@csrf_exempt
@api_view(['GET'])
def buscar_periodos_view(request, uc: BuscarPeriodos):
    dtos = uc.execute()
    return Response(PeriodoSerializer(dtos, many=True).data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['DELETE'])
def eliminar_periodo_view(request, uc: EliminarPeriodo):
    id_periodo = request.data.get('id_periodo')
    if not id_periodo:
        return Response({"error": "id_periodo es requerido"}, status=status.HTTP_400_BAD_REQUEST)
    success = uc.execute(id_periodo)
    return Response({"success": success}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['GET'])
def consultar_periodo_view(request, uc: ConsultarPeriodo, id_periodo: str):
    try:
        dto = uc.execute(id_periodo)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    return Response(PeriodoSerializer(dto).data, status=status.HTTP_200_OK)