# dtos.py
from dataclasses import dataclass
from personal.domain.personal import Rol

@dataclass
class PersonalDTO:
    id_personal: str | None
    nombre:       str
    rol:          Rol
    departamento: str
    correo:       str
    estado:       str

    @classmethod
    def create(cls, nombre, rol, departamento, correo, estado="Habilitado"):
        return cls(id_personal=None, nombre=nombre, rol=rol,
                   departamento=departamento, correo=correo, estado=estado)
