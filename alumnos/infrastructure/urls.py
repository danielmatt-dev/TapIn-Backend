from django.urls import path
from alumnos.infrastructure.views import registrar_alumno_view

urlpatterns = [
    path('registrar/', registrar_alumno_view),
]
