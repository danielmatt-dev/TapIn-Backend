from django.urls import path
from bloques.infrastructure.views_factory import (
    registrar_bloque_view_factory,
    buscar_bloques_view_factory,
    eliminar_bloque_view_factory
)

urlpatterns = [
    path('',       registrar_bloque_view_factory,   name='registrar_bloque'),
    path('listar', buscar_bloques_view_factory,     name='buscar_bloques'),
    path('eliminar', eliminar_bloque_view_factory,  name='eliminar_bloque'),
]
