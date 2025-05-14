from django.urls import path
from .views_factory import (
    registrar_personal_view_factory,
    eliminar_personal_view_factory,
    consultar_estado_personal_view_factory,
    actualizar_personal_view_factory
)

urlpatterns = [
    path('',            registrar_personal_view_factory,    name='registrar_personal'),
    path('eliminar/',   eliminar_personal_view_factory,     name='eliminar_personal'),
    path('listar/',     consultar_estado_personal_view_factory, name='consultar_estado_personal'),
    path('actualizar/', actualizar_personal_view_factory,   name='actualizar_personal'),
]