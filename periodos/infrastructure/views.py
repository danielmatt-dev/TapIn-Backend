from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from periodos.application.use_cases.use_cases import RegistrarPeriodo, BuscarPeriodos
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
