from dataclasses import dataclass
from datetime import date


@dataclass
class AlumnoDTO:
    id_alumno: str
    nombre_completo: str
    curp: str
    sexo: str
    correo_institucional: str
    fecha_nacimiento: date
    telefono_tutor: str
    es_silenciado: bool
    estado: str   

    @classmethod
    def from_empty(cls):
        return cls(
            id_alumno='',
            nombre_completo='',
            curp='',
            sexo='',
            correo_institucional='',
            fecha_nacimiento=date(1990, 1, 1),
            telefono_tutor='',
            estado='Activo'   
        )
