from injector import inject
from alumnos.application.use_cases.use_cases import ActualizarAlumno
from alumnos.domain.dtos import AlumnoDTO
from alumnos.domain.ports import AlumnoRepository
from alumnos.infrastructure.mapper.alumno_mapper import AlumnoMapper

class ActualizarAlumnoImpl(ActualizarAlumno):

    @inject
    def __init__(self,
                 repository: AlumnoRepository,
                 mapper: AlumnoMapper):
        self._repository = repository
        self._mapper = mapper

    def execute(self, dto: AlumnoDTO) -> AlumnoDTO:
        entidad = self._repository.obtener_por_id(dto.id_alumno)
        if entidad is None:
            raise Exception(f"Alumno con id {dto.id_alumno} no encontrado")

        entidad.nombre_completo       = dto.nombre_completo
        entidad.curp                  = dto.curp
        entidad.sexo                  = dto.sexo
        entidad.correo_institucional  = dto.correo_institucional
        entidad.fecha_nacimiento      = dto.fecha_nacimiento
        entidad.telefono_tutor        = dto.telefono_tutor

        actualizado = self._repository.actualizar(entidad)

        return self._mapper.to_dto(actualizado)
