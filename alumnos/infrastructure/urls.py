from django.urls import path
from views_factory import (
    registrar_alumno_view_factory,
    silenciar_alumno_view_factory,
    eliminar_alumno_view_factory,
    consultar_estado_alumnos_view_factory,
    actualizar_alumno_view_factory,
)

alumno_path = 'alumno'

urlpatterns = [
    path(f'{alumno_path}', registrar_alumno_view_factory, name='registrar_alumno'),
    path(f'{alumno_path}/silenciar', silenciar_alumno_view_factory, name='silenciar_alumno'),
    path(f'{alumno_path}/eliminar', eliminar_alumno_view_factory, name='eliminar_alumno'),
    path(f'{alumno_path}/listar', consultar_estado_alumnos_view_factory, name='consultar_estado_alumnos'),
    path(f'{alumno_path}/actualizar', actualizar_alumno_view_factory, name='actualizar_alumno'),
]
