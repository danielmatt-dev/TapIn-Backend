from dataclasses import dataclass
from nfc.domain.nfc import NFC
from alumnos.domain.dtos import AlumnoDTO  

@dataclass
class NFCDTO:
    id_nfc:        int | None
    identificador: str
    alumno:        AlumnoDTO
    estado:         str

    @classmethod
    def create(cls, identificador: str, alumno: AlumnoDTO, estado: str = "Habilitado"):
        return cls(id_nfc=None, identificador=identificador, alumno=alumno, estado=estado)
