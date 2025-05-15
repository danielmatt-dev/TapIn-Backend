from injector import inject
from typing import List
from bloques.domain.bloque import Bloque
from bloques.infrastructure.bloque_model import BloqueModel
from bloques.domain.ports import BloqueRepository
from bloques.infrastructure.mapper.bloque_mapper import BloqueMapper

class BloqueRepositoryImpl(BloqueRepository):
    @inject
    def __init__(self, mapper: BloqueMapper):
        self._mapper = mapper

    def registrar(self, bloque: Bloque) -> Bloque:
        model = self._mapper.to_model(bloque)
        model.save()
        return self._mapper.to_domain(model)

    def obtener_todos(self) -> List[Bloque]:
        qs = BloqueModel.objects.all()
        return [self._mapper.to_domain(m) for m in qs]

    def eliminar(self, id_bloque: str) -> bool:
        deleted, _ = BloqueModel.objects.filter(id_bloque=id_bloque).delete()
        return bool(deleted)

    def obtener_por_periodo(self, id_periodo: str) -> List[Bloque]:
        qs = BloqueModel.objects.filter(id_periodo=id_periodo)
        return [ self._mapper.to_domain(m) for m in qs ]