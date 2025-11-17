from django.urls import path
from inicio.views import inicio, otra, crear_auto, listar_autos

urlpatterns=[
     path('', inicio),
    path('otra/', otra),
    path('crear-auto/<marca>/<modelo>/', crear_auto),
    path('listado_autos/', listar_autos)
]