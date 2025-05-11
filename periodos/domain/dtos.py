from dataclasses import dataclass
from datetime import date, time

@dataclass
class PeriodoDTO:
    id_periodo: str
    nombre: str
    hora_entrada: time
    hora_salida: time
    fecha_inicio: date
    fecha_final: date
    estado: str
