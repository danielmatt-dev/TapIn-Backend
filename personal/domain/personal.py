# personal/domain/personal.py
from dataclasses import dataclass
from enum import Enum

class Rol(Enum):
    Administrativo = "Administrativo"
    Directivo      = "Directivo"

@dataclass
class Personal:
    id_personal: str
    nombre:       str
    rol:          Rol
    departamento: str
    correo:       str
    estado:       str
