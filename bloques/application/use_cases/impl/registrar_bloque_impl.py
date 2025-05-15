from injector import inject
from bloques.application.use_cases.use_cases import RegistrarBloque
from bloques.domain.dtos import BloqueDTO
from bloques.domain.bloque import Bloque
from bloques.domain.ports import BloqueRepository
from bloques.infrastructure.mapper.bloque_mapper import BloqueMapper

class RegistrarBloqueImpl(RegistrarBloque):

    @inject
    def __init__(
        self,
        repository: BloqueRepository,
        mapper: BloqueMapper
    ):
        self._repository = repository
        self._mapper     = mapper

    def execute(self, dto: BloqueDTO) -> BloqueDTO:
        entidad = Bloque(
            id_bloque  = dto.id_bloque,
            id_periodo = dto.id_periodo,  # ya es string
            nombre     = dto.nombre,
            meses      = dto.meses,
            estado     = dto.estado
        )
        creado = self._repository.registrar(entidad)
        return self._mapper.to_dto(creado)
