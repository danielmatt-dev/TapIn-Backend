from dataclasses import dataclass
from datetime import datetime

@dataclass
class InscripcionDTO:
    id_inscripcion: str
    id_alumno: str
    id_periodo: str
    fecha: datetime
    grado: str
    grupo: str
    estado: str

    @classmethod
    def nuevo(cls, id_alumno: str, id_periodo: str, fecha: datetime,
             grado: str, grupo: str, estado: str) -> "InscripcionDTO":
        return cls(
            id_inscripcion='',
            id_alumno=id_alumno,
            id_periodo=id_periodo,
            fecha=fecha,
            grado=grado,
            grupo=grupo,
            estado=estado
        )
