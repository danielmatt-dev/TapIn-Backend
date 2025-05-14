from injector import inject
from typing import List
from personal.application.use_cases.use_cases import ConsultarEstadoPersonal
from personal.domain.dtos import PersonalDTO
from personal.domain.ports import PersonalRepository
from personal.infrastructure.mapper.personal_mapper import PersonalMapper

class ConsultarEstadoPersonalImpl(ConsultarEstadoPersonal):

    @inject
    def __init__(self,
                 repository: PersonalRepository,
                 mapper: PersonalMapper):
        self._repository = repository
        self._mapper     = mapper

    def execute(self) -> List[PersonalDTO]:
        entidades = self._repository.obtener_todos()
        return [self._mapper.to_dto(e) for e in entidades]
