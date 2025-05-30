from dataclasses import dataclass
from datetime import date, time
from typing import List

from alertas.domain.alerta import Alerta
from alertas.infraestructure.alerta_model import AlertaModel
from alumnos.domain.dtos import AlumnoDTO
from inscripciones.domain.dtos import InscripcionDTO


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
              id_nfc: str,
              correo: str,
              fecha: date,
              hora: time,
              tipo_registro: str,
              tipo_acceso: str,
              estado: str):
        return cls(
            id_registro_asistencia=None,
            id_nfc=id_nfc,
            correo=correo,
            fecha=fecha,
            hora=hora,
            tipo_registro=tipo_registro,
            tipo_acceso=tipo_acceso,
            estado=estado,
        )


@dataclass
class AsistenciaResponse:
    id_registro_asistencia: int | None
    alumno: str
    correo: str
    grado: str
    grupo: str
    fecha: date
    hora: time
    tipo_registro: str
    tipo_acceso: str
    estado: str


@dataclass
class AsistenciasDTO:
    asistencias: List[AsistenciaResponse]
    alerta: List[Alerta]
