from injector import inject
from datetime import date
from typing import List
from asistencia.domain.asistencia import Asistencia
from asistencia.infrastructure.asistencia_model import AsistenciaModel
from asistencia.domain.ports import AsistenciaRepository
from asistencia.infrastructure.mapper.asistencia_mapper import AsistenciaMapper

class AsistenciaRepositoryImpl(AsistenciaRepository):

    @inject
    def __init__(self, mapper: AsistenciaMapper):
        self._mapper = mapper

    def registrar(self, a: Asistencia) -> Asistencia:
        model = self._mapper.to_model(a)
        model.save()
        return self._mapper.to_domain(model)

    def buscar_por_alumno(self, id_alumno: str) -> List[Asistencia]:
        qs = AsistenciaModel.objects.filter(id_alumno=id_alumno)
        return [ self._mapper.to_domain(m) for m in qs ]

    def consultar_por_dia(self, fecha: date) -> List[Asistencia]:
        qs = AsistenciaModel.objects.filter(fecha=fecha)
        return [ self._mapper.to_domain(m) for m in qs ]

    def consultar_por_periodo(self, fecha_inicio: date, fecha_fin: date) -> List[Asistencia]:
        qs = AsistenciaModel.objects.filter(fecha__range=(fecha_inicio, fecha_fin))
        return [ self._mapper.to_domain(m) for m in qs ]
