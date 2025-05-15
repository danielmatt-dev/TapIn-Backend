from injector import inject
from nfc.application.use_cases.use_cases import RegistrarNFC
from nfc.domain.dtos import NFCDTO
from nfc.domain.ports import NFCRepository

class RegistrarNFCImpl(RegistrarNFC):

    @inject
    def __init__(self, repo: NFCRepository):
        self._repo = repo

    def execute(self, dto: NFCDTO) -> NFCDTO:
        creado = self._repo.registrar(dto)
        return creado
