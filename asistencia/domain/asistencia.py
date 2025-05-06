from dataclasses import dataclass
from datetime import date, time

@dataclass
class Asistencia:
    id_registro_asistencia: int
    id_alumno: str
    fecha: date
    hora: time
    tipo_registro: str    # 'Normal','Justificada','Extraordinario','Tardío'
    tipo_acceso: str      # 'Entrada','Salida'
    estado: str           # 'Habilitado','Deshabilitado'
