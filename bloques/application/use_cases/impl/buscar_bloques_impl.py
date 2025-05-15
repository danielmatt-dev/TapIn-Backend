from injector import inject
from typing import List
from bloques.application.use_cases.use_cases import BuscarBloques
from bloques.domain.dtos import BloqueDTO
from bloques.domain.ports import BloqueRepository
from bloques.infrastructure.mapper.bloque_mapper import BloqueMapper

class BuscarBloquesImpl(BuscarBloques):
    @inject
    def __init__(self, repository: BloqueRepository, mapper: BloqueMapper):
        self._repository = repository
        self._mapper = mapper

    def execute(self) -> List[BloqueDTO]:
        dominios = self._repository.obtener_todos()
        return [self._mapper.to_dto(b) for b in dominios]
