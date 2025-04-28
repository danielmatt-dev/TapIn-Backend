from injector import Injector
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from alumnos.application.use_cases.use_cases import RegistrarAlumno
from alumnos.infrastructure.views import registrar_alumno_view
from injector_modules import InjectorModule

@csrf_exempt
def registrar_alumno_view_factory(request) -> Response:
    injector = Injector([InjectorModule])
    registrar_alumno_use_case = injector.get(RegistrarAlumno)
    return registrar_alumno_view(request, registrar_alumno_use_case)
