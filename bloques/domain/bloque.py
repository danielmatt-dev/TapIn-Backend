from dataclasses import dataclass

@dataclass
class Bloque:
    id_bloque: str
    id_periodo: str   # <-- string, no Periodo
    nombre: str
    meses: str
    estado: str
