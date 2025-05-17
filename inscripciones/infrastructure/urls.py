from django.urls import path
from .views_factory import (
    registrar_inscripcion_view_factory,
    buscar_inscripciones_view_factory,
    actualizar_periodo_view_factory,
    obtener_datos_view_factory,
)

urlpatterns = [
    path('',        registrar_inscripcion_view_factory,    name='nueva_inscripcion'),
    path('buscar',  buscar_inscripciones_view_factory,     name='buscar_inscripciones'),
    path('actualizar_periodo', actualizar_periodo_view_factory, name='actualizar_periodo'),
    path('datos_completos',    obtener_datos_view_factory,         name='obtener_datos_completos'),
]
