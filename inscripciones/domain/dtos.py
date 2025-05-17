from dataclasses import dataclass
from datetime import datetime
from typing import List

from alumnos.domain.dtos import AlumnoDTO
from periodos.domain.dtos import PeriodoDTO

@dataclass
class InscripcionDTO:
    id_inscripcion: str
    alumno: AlumnoDTO
    periodo: PeriodoDTO
    fecha: datetime
    grado: str
    grupo: str
    estado: str

    @classmethod
    def nuevo(cls,
              id_inscripcion: str,
              alumno: AlumnoDTO,
              periodo: PeriodoDTO,
              fecha: datetime,
              grado: str = '',
              grupo: str = '',
              estado: str = 'Activo'):
        return cls(id_inscripcion, alumno, periodo, fecha, grado, grupo, estado)

@dataclass
class DatosCompletosDTO:
    alumnos: List[AlumnoDTO]
    inscripciones: List[InscripcionDTO]
    periodos: List[PeriodoDTO]