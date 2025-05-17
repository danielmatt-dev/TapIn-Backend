from dataclasses import dataclass
from datetime import datetime

from alumnos.domain.alumno import Alumno
from periodos.domain.periodo import Periodo

@dataclass
class Inscripcion:
    id_inscripcion: str
    alumno: Alumno
    periodo: Periodo
    fecha: datetime
    grado: str
    grupo: str
    estado: str