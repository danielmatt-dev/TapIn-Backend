from dataclasses import dataclass

@dataclass
class BloqueDTO:
    id_bloque: str
    id_periodo: str    # aquí recibimos solo el id para la API
    nombre: str
    meses: str
    estado: str
