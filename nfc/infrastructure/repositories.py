from injector import inject
from typing import List, Optional
from nfc.domain.dtos import NFCDTO
from nfc.domain.ports import NFCRepository
from nfc.infrastructure.nfc_model import NFCModel
from nfc.infrastructure.mapper.nfc_mapper import NFCMapper

from alumnos.domain.ports import AlumnoRepository  # para obtener alumno completo

class NFCRepositoryImpl(NFCRepository):

    @inject
    def __init__(self,
                 mapper: NFCMapper,
                 alumno_repo: AlumnoRepository):
        self._mapper = mapper
        self._alumno_repo = alumno_repo

    def registrar(self, dto: NFCDTO) -> NFCDTO:
        model = NFCModel(
            identificador=dto.identificador,
            id_alumno=dto.alumno.id_alumno,
            estado=dto.estado
        )
        model.save()
        alumno = self._alumno_repo.obtener_por_id(model.id_alumno)
        dto.id_nfc = model.id_nfc
        dto.alumno = alumno
        return dto

    def eliminar(self, id_nfc: int) -> bool:
        deleted, _ = NFCModel.objects.filter(id_nfc=id_nfc).delete()
        return bool(deleted)

    def obtener_por_id(self, id_nfc: int) -> Optional[NFCDTO]:
        m = NFCModel.objects.filter(id_nfc=id_nfc).first()
        if not m:
            return None
        alumno = self._alumno_repo.obtener_por_id(m.id_alumno)
        return NFCDTO(
            id_nfc=m.id_nfc,
            identificador=m.identificador,
            alumno=alumno,
            estado=m.estado
        )

    def obtener_todos(self) -> List[NFCDTO]:
        resultados = []
        for m in NFCModel.objects.all():
            alumno = self._alumno_repo.obtener_por_id(m.id_alumno)
            resultados.append(NFCDTO(
                id_nfc=m.id_nfc,
                identificador=m.identificador,
                alumno=alumno,
                estado=m.estado
            ))
        return resultados

    def actualizar_estado(self, id_nfc: int, estado: str) -> bool:
        updated = NFCModel.objects.filter(id_nfc=id_nfc).update(estado=estado)
        return updated == 1
