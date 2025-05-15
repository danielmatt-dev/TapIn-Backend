from dataclasses import dataclass
from typing import List, Optional
from datetime import date, time

from bloques.domain.dtos import BloqueDTO

@dataclass
class PeriodoDTO:
    id_periodo: str
    nombre: str
    hora_entrada: time
    hora_salida: time
    fecha_inicio: date
    fecha_final: date
    estado: str
    bloques: List[BloqueDTO]    # <-- nuevo campo