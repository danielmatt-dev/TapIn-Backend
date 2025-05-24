from injector import Injector
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from personal.application.use_cases.use_cases import (
    RegistrarPersonal, EliminarPersonal,
    ConsultarEstadoPersonal, ActualizarPersonal, BuscarPersonalPorCorreo
)
from personal.infrastructure.views import (
    registrar_personal_view, eliminar_personal_view,
    consultar_estado_personal_view, actualizar_personal_view, buscar_por_correo
)
from personal.infrastructure.injector_modules import PersonalInjectorModule


@csrf_exempt
def login_with_google_view_factory(request) -> Response:
    inj = Injector([PersonalInjectorModule])
    uc = inj.get(BuscarPersonalPorCorreo)
    return buscar_por_correo(request, uc)

@csrf_exempt
def registrar_personal_view_factory(request) -> Response:
    inj = Injector([PersonalInjectorModule])
    uc  = inj.get(RegistrarPersonal)
    return registrar_personal_view(request, uc)

@csrf_exempt
def eliminar_personal_view_factory(request) -> Response:
    inj = Injector([PersonalInjectorModule])
    uc  = inj.get(EliminarPersonal)
    return eliminar_personal_view(request, uc)

@csrf_exempt
def consultar_estado_personal_view_factory(request) -> Response:
    inj = Injector([PersonalInjectorModule])
    uc  = inj.get(ConsultarEstadoPersonal)
    return consultar_estado_personal_view(request, uc)

@csrf_exempt
def actualizar_personal_view_factory(request) -> Response:
    inj = Injector([PersonalInjectorModule])
    uc  = inj.get(ActualizarPersonal)
    return actualizar_personal_view(request, uc)
