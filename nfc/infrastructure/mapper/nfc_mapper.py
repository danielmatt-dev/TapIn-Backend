from abc import ABC, abstractmethod
from nfc.infrastructure.nfc_model import NFCModel
from nfc.domain.nfc import NFC

class NFCMapper(ABC):

    @abstractmethod
    def to_model(self, domain: NFC) -> NFCModel:
        pass

    @abstractmethod
    def to_dto(self, domain: NFC) -> dict:
        pass
