from injector import Injector
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from periodos.application.use_cases.use_cases import RegistrarPeriodo, BuscarPeriodos, EliminarPeriodo
from periodos.infrastructure.views import registrar_periodo_view, buscar_periodos_view, eliminar_periodo_view
from periodos.infrastructure.injector_modules import PeriodosInjectorModule


@csrf_exempt
def registrar_periodo_view_factory(request) -> Response:
    inj = Injector([PeriodosInjectorModule])
    uc = inj.get(RegistrarPeriodo)
    return registrar_periodo_view(request, uc)


@csrf_exempt
def buscar_periodos_view_factory(request) -> Response:
    inj = Injector([PeriodosInjectorModule])
    uc = inj.get(BuscarPeriodos)
    return buscar_periodos_view(request, uc)


@csrf_exempt
def eliminar_periodo_view_factory(request) -> Response:
    inj = Injector([PeriodosInjectorModule])
    uc = inj.get(EliminarPeriodo)
    return eliminar_periodo_view(request, uc)
