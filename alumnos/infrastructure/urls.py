from django.urls import path
from views_factory import registrar_alumno_view_factory

alumno_path = 'alumno'

urlpatterns = [
    path(f'{alumno_path}', registrar_alumno_view_factory, name='registrar_alumno'),
]
