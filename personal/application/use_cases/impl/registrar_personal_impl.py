from injector import inject
from personal.application.use_cases.use_cases import RegistrarPersonal
from personal.domain.dtos import PersonalDTO
from personal.domain.ports import PersonalRepository
from personal.infrastructure.mapper.personal_mapper import PersonalMapper

class RegistrarPersonalImpl(RegistrarPersonal):

    @inject
    def __init__(self,
                 repository: PersonalRepository,
                 mapper: PersonalMapper):
        self._repository = repository
        self._mapper     = mapper

    def execute(self, dto: PersonalDTO) -> PersonalDTO:
        # crea entidad desde dto
        from personal.domain.personal import Personal
        entidad = Personal(
            id_personal=dto.id_personal,
            nombre     =dto.nombre,
            rol        =dto.rol,
            departamento=dto.departamento,
            correo     =dto.correo,
            estado     =dto.estado
        )
        creado = self._repository.registrar(entidad)
        return self._mapper.to_dto(creado)
