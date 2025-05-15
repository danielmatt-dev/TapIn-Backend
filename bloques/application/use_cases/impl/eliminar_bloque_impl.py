from injector import inject
from bloques.application.use_cases.use_cases import EliminarBloque
from bloques.domain.ports import BloqueRepository

class EliminarBloqueImpl(EliminarBloque):
    @inject
    def __init__(self, repository: BloqueRepository):
        self._repository = repository

    def execute(self, id_bloque: str) -> bool:
        return self._repository.eliminar(id_bloque)
