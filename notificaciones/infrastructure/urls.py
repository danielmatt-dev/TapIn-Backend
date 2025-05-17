from django.urls import path
from notificaciones.infrastructure.views_factory import (
    enviar_notificacion_view_factory,
    enviar_alerta_view_factory
)

urlpatterns = [
    path('notificaciones/', enviar_notificacion_view_factory, name='enviar_notificacion'),
    path('alertas/',      enviar_alerta_view_factory,      name='enviar_alerta'),
]
