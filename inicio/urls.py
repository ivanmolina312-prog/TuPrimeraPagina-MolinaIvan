from django.urls import path
from inicio.views import inicio, otra, crear_auto, listar_autos, ver_auto, actualizar_auto

urlpatterns=[
    path('', inicio, name='inicio'),
    path('otra/', otra, name='otra'),
    #path('crear-auto/<marca>/<modelo>/', crear_auto, name='crear'),
    path('ver-auto/auto_id', ver_auto, name='ver'),
    path('crear-auto/', crear_auto, name='crear'),
    path('actualizar-auto/<auto_id>/', actualizar_auto, name='actualizar'),
    path('listado_de_autos/', listar_autos, name='listado')
]