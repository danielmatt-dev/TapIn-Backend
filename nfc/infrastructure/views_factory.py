from injector import Injector
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from nfc.application.use_cases.use_cases import (
    RegistrarNFC, EliminarNFC, ListarNFC, ActualizarEstadoNFC
)
from nfc.infrastructure.views import (
    registrar_nfc_view, eliminar_nfc_view,
    listar_nfc_view, actualizar_estado_nfc_view
)
from nfc.infrastructure.injector_modules import NFCInjectorModule

@csrf_exempt
def registrar_nfc_view_factory(request) -> Response:
    inj = Injector([NFCInjectorModule])
    uc  = inj.get(RegistrarNFC)
    return registrar_nfc_view(request, uc)

@csrf_exempt
def eliminar_nfc_view_factory(request) -> Response:
    inj = Injector([NFCInjectorModule])
    uc  = inj.get(EliminarNFC)
    return eliminar_nfc_view(request, uc)

@csrf_exempt
def listar_nfc_view_factory(request) -> Response:
    inj = Injector([NFCInjectorModule])
    uc  = inj.get(ListarNFC)
    return listar_nfc_view(request, uc)

@csrf_exempt
def actualizar_estado_nfc_view_factory(request) -> Response:
    inj = Injector([NFCInjectorModule])
    uc  = inj.get(ActualizarEstadoNFC)
    return actualizar_estado_nfc_view(request, uc)
