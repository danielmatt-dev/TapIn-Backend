from dataclasses import dataclass
from alumnos.domain.alumno import Alumno  

@dataclass
class NFC:
    id_nfc:        int | None
    identificador: str
    alumno:        Alumno   
    estado:        str       # 'Habilitado'|'Deshabilitado'
