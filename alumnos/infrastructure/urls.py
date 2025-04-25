from django.urls import path
from views_factory import registrar_alumno_view_factory

urlpatterns = [
    path('registrar/', registrar_alumno_view_factory),
]
