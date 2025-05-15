from injector import Injector
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from bloques.application.use_cases.use_cases import (
    RegistrarBloque, BuscarBloques, EliminarBloque
)
from bloques.infrastructure.views import (
    registrar_bloque_view, buscar_bloques_view, eliminar_bloque_view
)
from bloques.infrastructure.injector_modules import BloquesInjectorModule

@csrf_exempt
def registrar_bloque_view_factory(request) -> Response:
    inj = Injector([BloquesInjectorModule])
    uc  = inj.get(RegistrarBloque)
    return registrar_bloque_view(request, uc)

@csrf_exempt
def buscar_bloques_view_factory(request) -> Response:
    inj = Injector([BloquesInjectorModule])
    uc  = inj.get(BuscarBloques)
    return buscar_bloques_view(request, uc)

@csrf_exempt
def eliminar_bloque_view_factory(request) -> Response:
    inj = Injector([BloquesInjectorModule])
    uc  = inj.get(EliminarBloque)
    return eliminar_bloque_view(request, uc)
