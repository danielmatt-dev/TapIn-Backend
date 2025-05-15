from django.urls import path
from .views_factory import (
    registrar_nfc_view_factory,
    eliminar_nfc_view_factory,
    listar_nfc_view_factory,
    actualizar_estado_nfc_view_factory
)

urlpatterns = [
    path('',            registrar_nfc_view_factory,        name='registrar_nfc'),        # POST
    path('eliminar/',   eliminar_nfc_view_factory,         name='eliminar_nfc'),         # DELETE
    path('listar/',     listar_nfc_view_factory,           name='listar_nfc'),           # GET
    path('actualizar/', actualizar_estado_nfc_view_factory, name='actualizar_estado_nfc'), # POST
]
