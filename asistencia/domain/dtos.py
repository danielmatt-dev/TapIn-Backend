from dataclasses import dataclass
from datetime import date, time

@dataclass
class AsistenciaDTO:
    id_registro_asistencia: int | None
    id_alumno: str
    fecha: date
    hora: time
    tipo_registro: str
    tipo_acceso: str
    estado: str

    @classmethod
    def nuevo(cls,
              id_alumno: str,
              fecha: date,
              hora: time,
              tipo_registro: str,
              tipo_acceso: str,
              estado: str):
        return cls(
            id_registro_asistencia=None,
            id_alumno=id_alumno,
            fecha=fecha,
            hora=hora,
            tipo_registro=tipo_registro,
            tipo_acceso=tipo_acceso,
            estado=estado,
        )
