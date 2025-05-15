from django.contrib import admin
from django.urls import include, path

from config.google_login import GoogleLogin

api_path = 'scolaris'

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/social/google/', GoogleLogin.as_view(), name='google_login'),
    path(f'{api_path}/', include('alumnos.infrastructure.urls')),
    path(f'{api_path}/asistencia/', include('asistencia.infrastructure.urls')),
    path(f'{api_path}/inscripcion/', include('inscripciones.infrastructure.urls')),
    path(f'{api_path}/periodos/', include('periodos.infrastructure.urls')),
    path(f'{api_path}/personal/', include('personal.infrastructure.urls')),
    path(f'{api_path}/nfc/', include('nfc.infrastructure.urls')),
    path(f'{api_path}/bloques/', include('bloques.infrastructure.urls')),

]
