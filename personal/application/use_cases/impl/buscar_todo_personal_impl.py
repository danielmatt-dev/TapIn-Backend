from injector import inject

from personal.application.use_cases.use_cases import BuscarPersonalPorCorreo
from personal.domain.dtos import PersonalDTO
from personal.domain.ports import PersonalRepository
from personal.infrastructure.mapper.personal_mapper import PersonalMapper


class BuscarPersonalPorCorreoImpl(BuscarPersonalPorCorreo):

    @inject
    def __init__(self, repository: PersonalRepository, mapper: PersonalMapper):
        self._repository = repository
        self._mapper = mapper

    def execute(self, correo: str) -> PersonalDTO | None:
        personal = self._repository.obtener_por_correo(correo=correo)
        if personal is None:
            return None
        return self._mapper.to_dto(personal)
