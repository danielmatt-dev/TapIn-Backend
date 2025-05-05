from injector import Injector
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from alumnos.application.use_cases.use_cases import (
    RegistrarAlumno,
    SilenciarAlumno,
    EliminarAlumno,
    ConsultarEstadoAlumnos,
    ActualizarAlumno
)
from alumnos.infrastructure.views import (
    registrar_alumno_view,
    silenciar_alumno_view,
    eliminar_alumno_view,
    consultar_estado_alumnos_view,
    actualizar_alumno_view
)
from injector_modules import InjectorModule


@csrf_exempt
def registrar_alumno_view_factory(request) -> Response:
    injector = Injector([InjectorModule])
    registrar_alumno_use_case = injector.get(RegistrarAlumno)
    return registrar_alumno_view(request, registrar_alumno_use_case)


@csrf_exempt
def silenciar_alumno_view_factory(request) -> Response:
    injector = Injector([InjectorModule])
    silenciar_alumno_use_case = injector.get(SilenciarAlumno)
    return silenciar_alumno_view(request, silenciar_alumno_use_case)


@csrf_exempt
def eliminar_alumno_view_factory(request) -> Response:
    injector = Injector([InjectorModule])
    eliminar_alumno_use_case = injector.get(EliminarAlumno)
    return eliminar_alumno_view(request, eliminar_alumno_use_case)


@csrf_exempt
def consultar_estado_alumnos_view_factory(request) -> Response:
    injector = Injector([InjectorModule])
    consultar_estado_alumnos_use_case = injector.get(ConsultarEstadoAlumnos)
    return consultar_estado_alumnos_view(request, consultar_estado_alumnos_use_case)

@csrf_exempt
def actualizar_alumno_view_factory(request) -> Response:
    injector = Injector([InjectorModule])
    use_case = injector.get(ActualizarAlumno)
    return actualizar_alumno_view(request, use_case)