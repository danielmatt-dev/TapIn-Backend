from django.urls import path

from .views_factory import registrar_periodo_view_factory, buscar_periodos_view_factory, eliminar_periodo_view_factory, consultar_periodo_view_factory

urlpatterns = [
    path('', registrar_periodo_view_factory, name='registrar_periodo'),  
    path('listar', buscar_periodos_view_factory, name='buscar_periodos'), 
    path('eliminar', eliminar_periodo_view_factory, name='eliminar_periodo'),
    path('<str:id_periodo>', consultar_periodo_view_factory, name='consultar_periodo'),
]
