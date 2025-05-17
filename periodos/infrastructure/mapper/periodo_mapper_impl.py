from periodos.domain.periodo import Periodo
from periodos.domain.dtos import PeriodoDTO
from periodos.infrastructure.periodo_model import PeriodoModel
from periodos.infrastructure.mapper.periodo_mapper import PeriodoMapper
from bloques.infrastructure.mapper.bloque_mapper_impl import BloqueMapperImpl


class PeriodoMapperImpl(PeriodoMapper):

    def to_domain(self, model: PeriodoModel) -> Periodo:
        return Periodo(
            id_periodo=model.id_periodo,
            nombre=model.nombre,
            hora_entrada=model.hora_entrada,
            hora_salida=model.hora_salida,
            fecha_inicio=model.fecha_inicio,
            fecha_final=model.fecha_final,
            estado=model.estado
        )

    def to_model(self, domain: Periodo) -> PeriodoModel:
        return PeriodoModel(
            id_periodo=domain.id_periodo,
            nombre=domain.nombre,
            hora_entrada=domain.hora_entrada,
            hora_salida=domain.hora_salida,
            fecha_inicio=domain.fecha_inicio,
            fecha_final=domain.fecha_final,
            estado=domain.estado
        )

    def to_dto(self, domain: Periodo) -> PeriodoDTO:
        bloques_dto = [
            BloqueMapperImpl().to_dto(b)
            for b in getattr(domain, 'bloques', [])
    ]
        return PeriodoDTO(
            id_periodo = domain.id_periodo,
            nombre      = domain.nombre,
            hora_entrada= domain.hora_entrada,
            hora_salida = domain.hora_salida,
            fecha_inicio= domain.fecha_inicio,
            fecha_final = domain.fecha_final,
            estado      = domain.estado,
            bloques     = bloques_dto
    )

    def to_domain_from_dto(self, dto: PeriodoDTO) -> Periodo:
        return Periodo(
            id_periodo=dto.id_periodo,
            nombre=dto.nombre,
            hora_entrada=dto.hora_entrada,
            hora_salida=dto.hora_salida,
            fecha_inicio=dto.fecha_inicio,
            fecha_final=dto.fecha_final,
            estado=dto.estado
        )
