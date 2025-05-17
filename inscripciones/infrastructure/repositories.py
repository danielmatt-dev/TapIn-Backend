from injector import inject
from typing import List
from inscripciones.domain.inscripcion import Inscripcion
from inscripciones.infrastructure.inscripcion_model import InscripcionModel
from inscripciones.domain.ports import InscripcionRepository
from inscripciones.infrastructure.mapper.inscripcion_mapper import InscripcionMapper

class InscripcionRepositoryImpl(InscripcionRepository):

    @inject
    def __init__(self, mapper: InscripcionMapper):
        self._mapper = mapper

    def registrar(self, inscripcion: Inscripcion) -> InscripcionModel:
        model = self._mapper.to_model(inscripcion)
        model.save()
        return model

    def buscar_por_alumno(self, id_alumno: str) -> List[InscripcionModel]:
        return list(InscripcionModel.objects.filter(alumno_id=id_alumno))

    def actualizar_periodo(self, id_inscripcion: str, id_periodo: str) -> bool:
        updated = (
            InscripcionModel.objects
                .filter(pk=id_inscripcion)
                .update(periodo_id=id_periodo)
        )
        return updated == 1

    def vaciar(self) -> bool:
        deleted_count, _ = InscripcionModel.objects.all().delete()
        return bool(deleted_count)
    
    def buscar_todas(self) -> list[InscripcionModel]:

        return list(InscripcionModel.objects.all())
