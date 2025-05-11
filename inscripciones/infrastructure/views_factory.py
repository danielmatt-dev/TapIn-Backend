from injector import Injector
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from inscripciones.application.use_cases.use_cases import (
    NuevaInscripcion, BuscarInscripciones, ActualizarPeriodo, VaciarInscripciones
)
from inscripciones.infrastructure.views import (
    registrar_inscripcion_view, buscar_inscripciones_view,
    actualizar_periodo_view, vaciar_inscripciones_view
)
from inscripciones.infrastructure.injector_modules import InscripcionesInjectorModule

@csrf_exempt
def registrar_inscripcion_view_factory(request) -> Response:
    inj = Injector([InscripcionesInjectorModule])
    uc  = inj.get(NuevaInscripcion)
    return registrar_inscripcion_view(request, uc)

@csrf_exempt
def buscar_inscripciones_view_factory(request) -> Response:
    inj = Injector([InscripcionesInjectorModule])
    uc  = inj.get(BuscarInscripciones)
    return buscar_inscripciones_view(request, uc)

@csrf_exempt
def actualizar_periodo_view_factory(request) -> Response:
    inj = Injector([InscripcionesInjectorModule])
    uc  = inj.get(ActualizarPeriodo)
    return actualizar_periodo_view(request, uc)

@csrf_exempt
def vaciar_inscripciones_view_factory(request) -> Response:
    inj = Injector([InscripcionesInjectorModule])
    uc  = inj.get(VaciarInscripciones)
    return vaciar_inscripciones_view(request, uc)
