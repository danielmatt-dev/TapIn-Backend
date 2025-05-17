# inscripciones/application/use_cases/impl/obtener_datos_impl.py

from inscripciones.application.use_cases.use_cases import ObtenerDatos
from inscripciones.domain.dtos import DatosCompletosDTO
from alumnos.infrastructure.repositories import AlumnoRepositoryImpl
from inscripciones.infrastructure.repositories import InscripcionRepositoryImpl
from periodos.infrastructure.repositories import PeriodoRepositoryImpl
from alumnos.infrastructure.mapper.alumno_mapper_impl import AlumnoMapperImpl
from inscripciones.infrastructure.mapper.inscripcion_mapper_impl import InscripcionMapperImpl
from periodos.infrastructure.mapper.periodo_mapper_impl import PeriodoMapperImpl

class ObtenerDatosImpl(ObtenerDatos):
    def __init__(self,
                 alumno_repo: AlumnoRepositoryImpl,
                 insc_repo: InscripcionRepositoryImpl,
                 periodo_repo: PeriodoRepositoryImpl):
        self._alumno_repo   = alumno_repo
        self._insc_repo     = insc_repo
        self._periodo_repo  = periodo_repo
        self._alumno_map    = AlumnoMapperImpl()
        self._insc_map      = InscripcionMapperImpl()
        self._periodo_map   = PeriodoMapperImpl()

    def execute(self) -> DatosCompletosDTO:

        alumnos_model    = self._alumno_repo.buscar_todos()
        inscripciones_mod= self._insc_repo.buscar_todas()
        periodos_model   = self._periodo_repo.buscar_todos()

        alumnos_dto      = [
            self._alumno_map.to_dto(self._alumno_map.to_domain(a))
            for a in alumnos_model
        ]
        inscripciones_dto= [
            self._insc_map.to_dto(self._insc_map.to_domain(i))
            for i in inscripciones_mod
        ]
        periodos_dto     = [
            self._periodo_map.to_dto(self._periodo_map.to_domain(p))
            for p in periodos_model
        ]

        return DatosCompletosDTO(
            alumnos       = alumnos_dto,
            inscripciones = inscripciones_dto,
            periodos      = periodos_dto
        )
