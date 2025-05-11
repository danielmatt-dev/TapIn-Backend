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

    def registrar(self, inscripcion: Inscripcion) -> Inscripcion:
        model = self._mapper.to_model(inscripcion)
        model.save()
        return self._mapper.to_domain(model)

    def buscar_por_alumno(self, id_alumno: str) -> List[Inscripcion]:
        qs = InscripcionModel.objects.filter(id_alumno=id_alumno)
        return [ self._mapper.to_domain(m) for m in qs ]

    def actualizar_periodo(self, id_inscripcion: str, nuevo_periodo: str) -> bool:
        updated = InscripcionModel.objects \
            .filter(id_inscripcion=id_inscripcion) \
            .update(id_periodo=nuevo_periodo)
        return updated == 1

    def vaciar_por_periodo(self, id_periodo: str) -> int:
        deleted, _ = InscripcionModel.objects.filter(id_periodo=id_periodo).delete()
        return deleted
