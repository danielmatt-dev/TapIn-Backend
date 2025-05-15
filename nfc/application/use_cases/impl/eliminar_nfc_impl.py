from injector import inject
from nfc.application.use_cases.use_cases import EliminarNFC
from nfc.domain.ports import NFCRepository

class EliminarNFCImpl(EliminarNFC):

    @inject
    def __init__(self, repo: NFCRepository):
        self._repo = repo

    def execute(self, id_nfc: int) -> bool:
        return self._repo.eliminar(id_nfc)
