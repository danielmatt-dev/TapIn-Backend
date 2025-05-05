from alumnos.domain.alumno import Alumno
from alumnos.domain.dtos import AlumnoDTO
from alumnos.infrastructure.alumno_model import AlumnoModel

from alumnos.infrastructure.mapper.alumno_mapper import AlumnoMapper


class AlumnoMapperImpl(AlumnoMapper):

    def to_domain(self, model: AlumnoModel) -> Alumno:
        return Alumno(
            id_alumno=model.id_alumno,
            nombre_completo=model.nombre_completo,
            curp=model.curp,
            sexo=model.sexo,
            correo_institucional=model.correo_institucional,
            fecha_nacimiento=model.fecha_nacimiento,
            telefono_tutor=model.telefono_tutor,
            es_silenciado=model.es_silenciado,
            estado=model.estado
        )

    def to_model(self, domain: Alumno) -> AlumnoModel:
        return AlumnoModel(
            id_alumno=domain.id_alumno,
            nombre_completo=domain.nombre_completo,
            curp=domain.curp,
            sexo=domain.sexo,
            correo_institucional=domain.correo_institucional,
            fecha_nacimiento=domain.fecha_nacimiento,
            telefono_tutor=domain.telefono_tutor,
            es_silenciado=domain.es_silenciado,
            estado=domain.estado
        )

    def to_dto(self, domain: Alumno) -> AlumnoDTO:
        return AlumnoDTO(
            id_alumno=domain.id_alumno,
            nombre_completo=domain.nombre_completo,
            curp=domain.curp,
            sexo=domain.sexo,
            correo_institucional=domain.correo_institucional,
            fecha_nacimiento=domain.fecha_nacimiento,
            telefono_tutor=domain.telefono_tutor,
            es_silenciado=domain.es_silenciado,
            estado=domain.estado  
        )
