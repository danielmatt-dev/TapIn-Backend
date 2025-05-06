from django.urls import path
from asistencia.infrastructure.views_factory import (
    registrar_asistencia_view_factory,
    buscar_asistencias_view_factory,
    consultar_por_dia_view_factory,
    consultar_por_periodo_view_factory
)

base = 'asistencia'

urlpatterns = [
    path(f'{base}',        registrar_asistencia_view_factory,      name='registrar_asistencia'),
    path(f'{base}/buscar', buscar_asistencias_view_factory,      name='buscar_asistencias'),
    path(f'{base}/dia',    consultar_por_dia_view_factory,       name='consultar_asistencias_dia'),
    path(f'{base}/periodo',consultar_por_periodo_view_factory,   name='consultar_asistencias_periodo'),
]
