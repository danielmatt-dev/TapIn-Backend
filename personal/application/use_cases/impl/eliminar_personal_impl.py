from injector import inject
from personal.application.use_cases.use_cases import EliminarPersonal
from personal.domain.ports import PersonalRepository

class EliminarPersonalImpl(EliminarPersonal):

    @inject
    def __init__(self, repository: PersonalRepository):
        self._repository = repository

    def execute(self, id_personal: str) -> bool:
        return self._repository.eliminar(id_personal)
