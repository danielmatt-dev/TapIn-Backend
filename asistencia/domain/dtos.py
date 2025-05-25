from dataclasses import dataclass
from datetime import date, time

@dataclass
class AsistenciaDTO:
    id_registro_asistencia: int | None
    id_nfc: str | None
    correo: str | None
    fecha: date
    hora: time
    tipo_registro: str
    tipo_acceso: str
    estado: str

    @classmethod
    def nuevo(cls,
              id_alumno: str,
              correo: str,
              fecha: date,
              hora: time,
              tipo_registro: str,
              tipo_acceso: str,
              estado: str):
        return cls(
            id_registro_asistencia=None,
            id_nfc=id_alumno,
            correo=correo,
            fecha=fecha,
            hora=hora,
            tipo_registro=tipo_registro,
            tipo_acceso=tipo_acceso,
            estado=estado,
        )
