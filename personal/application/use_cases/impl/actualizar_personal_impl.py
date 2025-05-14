from injector import inject
from personal.application.use_cases.use_cases import ActualizarPersonal
from personal.domain.dtos import PersonalDTO
from personal.domain.ports import PersonalRepository
from personal.infrastructure.mapper.personal_mapper import PersonalMapper

class ActualizarPersonalImpl(ActualizarPersonal):

    @inject
    def __init__(self,
                 repository: PersonalRepository,
                 mapper: PersonalMapper):
        self._repository = repository
        self._mapper     = mapper

    def execute(self, dto: PersonalDTO) -> PersonalDTO:
        entidad = self._repository.obtener_por_id(dto.id_personal)
        if entidad is None:
            raise Exception(f"Personal con id {dto.id_personal} no encontrado")

        entidad.nombre      = dto.nombre
        entidad.rol         = dto.rol
        entidad.departamento= dto.departamento
        entidad.correo      = dto.correo
        entidad.estado      = dto.estado

        actualizado = self._repository.actualizar(entidad)
        return self._mapper.to_dto(actualizado)
