from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from bloques.application.use_cases.use_cases import (
    RegistrarBloque, BuscarBloques, EliminarBloque
)
from bloques.domain.dtos import BloqueDTO
from bloques.infrastructure.serializers import BloqueSerializer

@csrf_exempt
@api_view(['POST'])
def registrar_bloque_view(request, uc: RegistrarBloque):
    ser = BloqueSerializer(data=request.data)
    if not ser.is_valid():
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    dto = BloqueDTO(**ser.validated_data)
    creado = uc.execute(dto)
    return Response(BloqueSerializer(creado).data, status=status.HTTP_201_CREATED)

@csrf_exempt
@api_view(['GET'])
def buscar_bloques_view(request, uc: BuscarBloques):
    dtos = uc.execute()
    return Response(BloqueSerializer(dtos, many=True).data, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(['DELETE'])
def eliminar_bloque_view(request, uc: EliminarBloque):
    id_bloque = request.data.get('id_bloque')
    if not id_bloque:
        return Response({'error': 'id_bloque es requerido'}, status=status.HTTP_400_BAD_REQUEST)
    eliminado = uc.execute(id_bloque)
    return Response({'success': eliminado}, status=status.HTTP_200_OK)
