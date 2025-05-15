from injector import inject
from nfc.application.use_cases.use_cases import ActualizarEstadoNFC
from nfc.domain.ports import NFCRepository

class ActualizarEstadoNFCImpl(ActualizarEstadoNFC):

    @inject
    def __init__(self, repo: NFCRepository):
        self._repo = repo

    def execute(self, id_nfc: int, estado: str) -> bool:
        return self._repo.actualizar_estado(id_nfc, estado)
