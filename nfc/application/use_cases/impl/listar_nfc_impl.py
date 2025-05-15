from injector import inject
from typing import List
from nfc.application.use_cases.use_cases import ListarNFC
from nfc.domain.dtos import NFCDTO
from nfc.domain.ports import NFCRepository

class ListarNFCImpl(ListarNFC):

    @inject
    def __init__(self, repo: NFCRepository):
        self._repo = repo

    def execute(self) -> List[NFCDTO]:
        return self._repo.obtener_todos()
