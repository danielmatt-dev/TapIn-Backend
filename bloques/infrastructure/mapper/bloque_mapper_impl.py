from bloques.domain.bloque import Bloque
from bloques.domain.dtos import BloqueDTO
from bloques.infrastructure.bloque_model import BloqueModel
from bloques.infrastructure.mapper.bloque_mapper import BloqueMapper

class BloqueMapperImpl(BloqueMapper):
    def to_domain(self, model: BloqueModel) -> Bloque:
        return Bloque(
            id_bloque = model.id_bloque,
            id_periodo= model.id_periodo,
            nombre    = model.nombre,
            meses     = model.meses,
            estado    = model.estado
        )

    def to_model(self, domain: Bloque) -> BloqueModel:
        return BloqueModel(
            id_bloque = domain.id_bloque,
            id_periodo= domain.id_periodo,
            nombre    = domain.nombre,
            meses     = domain.meses,
            estado    = domain.estado
        )

    def to_dto(self, domain: Bloque) -> BloqueDTO:
        return BloqueDTO(
            id_bloque = domain.id_bloque,
            id_periodo= domain.id_periodo,
            nombre    = domain.nombre,
            meses     = domain.meses,
            estado    = domain.estado
        )
