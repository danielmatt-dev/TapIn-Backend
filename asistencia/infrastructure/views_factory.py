from injector import Injector
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from alertas.domain.generar_alertas import GenerarAlertas
from alumnos.infrastructure.injector_modules import AlumnoInjectorModule
from asistencia.application.use_cases.use_cases import (
    RegistrarAsistencia,
    BuscarAsistencias,
    ConsultarAsistenciasDelDia,
    ConsultarAsistenciasDelPeriodo
)
from asistencia.infrastructure.views import (
    registrar_asistencia_view,
    buscar_asistencias_view,
    consultar_por_dia_view,
    consultar_por_periodo_view
)

from asistencia.infrastructure.injector_modules import AsistenciaInjectorModule

@csrf_exempt
def registrar_asistencia_view_factory(request) -> Response:
    inj = Injector([AsistenciaInjectorModule])
    uc  = inj.get(RegistrarAsistencia)
    return registrar_asistencia_view(request, uc)

@csrf_exempt
def buscar_asistencias_view_factory(request) -> Response:
    inj = Injector([AsistenciaInjectorModule])
    uc  = inj.get(BuscarAsistencias)
    return buscar_asistencias_view(request, uc)

@csrf_exempt
def consultar_por_dia_view_factory(request) -> Response:
    inj = Injector([AsistenciaInjectorModule])
    uc  = inj.get(ConsultarAsistenciasDelDia)
    return consultar_por_dia_view(request, uc)

@csrf_exempt
def consultar_por_periodo_view_factory(request) -> Response:
    inj = Injector([AsistenciaInjectorModule])
    inj_alumno = Injector([AlumnoInjectorModule])
    uc  = inj.get(ConsultarAsistenciasDelPeriodo)
    uc2 = inj_alumno.get(GenerarAlertas)
    return consultar_por_periodo_view(request, uc, uc2)
