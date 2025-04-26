from injector import inject

from alumnos.application.use_cases.use_cases import RegistrarAlumno
from alumnos.domain.alumno import Alumno
from alumnos.domain.dtos import AlumnoDTO
from alumnos.domain.ports import AlumnoRepository
from alumnos.infrastructure.mapper.alumno_mapper import AlumnoMapper


class RegistrarAlumnoImpl(RegistrarAlumno):

    @inject
    def __init__(self, repository: AlumnoRepository, mapper: AlumnoMapper):
        self._repository = repository
        self._mapper = mapper

    def execute(self, dto: AlumnoDTO) -> AlumnoDTO:
        alumno = Alumno(
            id_alumno=dto.id_alumno,
            nombre_completo=dto.nombre_completo,
            curp=dto.curp,
            sexo=dto.sexo,
            correo_institucional=dto.correo_institucional,
            fecha_nacimiento=dto.fecha_nacimiento,
            telefono_tutor=dto.telefono_tutor,
            es_silenciado=False,
            estado="Activo"
        )
        alumno_registrado = self._repository.registrar(alumno)

        return self._mapper.to_dto(alumno_registrado)
