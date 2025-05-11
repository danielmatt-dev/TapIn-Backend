from dataclasses import dataclass
from datetime import datetime

@dataclass
class Inscripcion:
    id_inscripcion: str
    id_alumno: str
    id_periodo: str
    fecha: datetime
    grado: str
    grupo: str
    estado: str
