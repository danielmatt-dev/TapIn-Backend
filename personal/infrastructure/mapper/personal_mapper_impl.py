from personal.domain.personal import Personal
from personal.domain.dtos import PersonalDTO
from personal.infrastructure.personal_model import PersonalModel
from personal.infrastructure.mapper.personal_mapper import PersonalMapper

class PersonalMapperImpl(PersonalMapper):

    def to_domain(self, model: PersonalModel) -> Personal:
        return Personal(
            id_personal = model.id_personal,
            nombre      = model.nombre,
            rol         = model.rol,
            departamento= model.departamento,
            correo      = model.correo,
            estado      = model.estado
        )

    def to_model(self, domain: Personal) -> PersonalModel:
        return PersonalModel(
            id_personal = domain.id_personal,
            nombre      = domain.nombre,
            rol         = domain.rol.value if hasattr(domain.rol, 'value') else domain.rol,
            departamento= domain.departamento,
            correo      = domain.correo,
            estado      = domain.estado
        )

    def to_dto(self, domain: Personal) -> PersonalDTO:
        return PersonalDTO(
            id_personal = domain.id_personal,
            nombre      = domain.nombre,
            rol         = domain.rol,
            departamento= domain.departamento,
            correo      = domain.correo,
            estado      = domain.estado
        )
