from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from nfc.infrastructure.mapper.nfc_mapper import NFCMapper
from nfc.infrastructure.serializers import NFCOutputSerializer
from nfc.application.use_cases.use_cases import (
    RegistrarNFC, EliminarNFC, ListarNFC, ActualizarEstadoNFC
)
from nfc.domain.dtos import NFCDTO
from alumnos.domain.dtos import AlumnoDTO

@api_view(['POST'])
def registrar_nfc_view(request, registrar: RegistrarNFC):
    # recibimos identificador + id_alumno
    identificador = request.data['identificador']
    id_alumno     = request.data['id_alumno']
    alumno_dto    = AlumnoDTO(id_alumno=id_alumno,  # campos mínimos, o usa repositorio
                              nombre_completo='', curp='',
                              sexo='', correo_institucional='',
                              fecha_nacimiento=None,
                              telefono_tutor='', es_silenciado=False,
                              estado='')
    dto = NFCDTO.create(identificador, alumno_dto)
    creado = registrar.execute(dto)
    return Response(NFCOutputSerializer(creado).data,
                    status=status.HTTP_201_CREATED)

@api_view(['GET'])
def listar_nfc_view(request, listar: ListarNFC):
    dtos = listar.execute()
    return Response(NFCOutputSerializer(dtos, many=True).data,
                    status=status.HTTP_200_OK)

@api_view(['DELETE'])
def eliminar_nfc_view(request, eliminar: EliminarNFC):
    id_nfc = request.data.get('id_nfc')
    if id_nfc is None:
        return Response({"error":"id_nfc es requerido"},
                        status=status.HTTP_400_BAD_REQUEST)
    ok = eliminar.execute(id_nfc)
    return Response({"success": ok}, status=status.HTTP_200_OK)

@api_view(['POST'])
def actualizar_estado_nfc_view(request, actualizar: ActualizarEstadoNFC):
    id_nfc = request.data.get('id_nfc')
    estado = request.data.get('estado')
    if id_nfc is None or estado is None:
        return Response({"error":"id_nfc y estado son requeridos"},
                        status=status.HTTP_400_BAD_REQUEST)
    ok = actualizar.execute(id_nfc, estado)
    return Response({"success": ok}, status=status.HTTP_200_OK)
