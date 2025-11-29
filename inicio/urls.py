from django.urls import path
from inicio.views import inicio, otra, crear_auto, listar_autos, ver_auto, ActualizarAuto, EliminarAuto

urlpatterns=[
    path('', inicio, name='inicio'),
    path('otra/', otra, name='otra'),
    #path('crear-auto/<marca>/<modelo>/', crear_auto, name='crear'),
    path('ver-auto/auto_id', ver_auto, name='ver'),
    path('crear-auto/', crear_auto, name='crear'),
    path('actualizar-auto/<pk>/', ActualizarAuto.as_view(), name='actualizar'),
    path('eliminar-auto/<pk>/', EliminarAuto.as_view(), name='eliminar'),
    path('listado-autos/', listar_autos, name='listado')
]