from django.urls import path
from .views import agregar_invitado, lista_invitados, eliminar_invitado, confirmar_asistencia

urlpatterns = [
    path('agregar/', agregar_invitado, name='agregar_invitado'),
    path('lista/', lista_invitados, name='lista_invitados'),
    path('eliminar/<int:id>/', eliminar_invitado, name='eliminar_invitado'),
    path('confirmar-asistencia/<int:id>/', confirmar_asistencia, name='confirmar_asistencia'),
]
