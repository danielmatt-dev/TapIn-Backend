from dataclasses import dataclass
from datetime import date


@dataclass
class Alumno:
    id_alumno: str
    nombre_completo: str
    curp: str
    sexo: str
    correo_institucional: str
    fecha_nacimiento: date
    telefono_tutor: str
    es_silenciado: bool
    estado: str
