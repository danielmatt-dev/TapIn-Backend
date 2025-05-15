from nfc.domain.dtos import NFCDTO
from nfc.infrastructure.mapper.nfc_mapper import NFCMapper

class NFCMapperImpl(NFCMapper):

    def to_dto(self, dto: NFCDTO) -> NFCDTO:
        return dto

    def to_model(self, dto: NFCDTO):
        pass

    def to_domain(self, dto: NFCDTO):
        pass
