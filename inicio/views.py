from django.shortcuts import render, redirect
from django.http import HttpResponse 
from inicio.models import Auto
from inicio.forms import CrearAuto
from django.views.generic.edit import UpdateView
def inicio(request):
   # return HttpResponse ('<h1>Hola soy el proyercto</h1>')
    return  render(request, 'inicio.html')

def otra(request):
  
    return  render(request, 'otra.html')

def crear_auto (request, marca, modelo):
    auto = None
    if request.method == 'POST':
        formulario = CrearAuto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data

            auto = Auto(marca=info.get('marca'), modelo=info.get('modelo'))
            auto.save()

            return redirect('listado')
    else:
        formulario = CrearAuto()

    return render(request, 'crear_auto.html', {'formulario': formulario})

def listar_autos(request):
    autos = Auto.objects.all()
    return render(request, 'listar_autos.html', {'listado_de_autos': autos})

def ver_auto(request, auto_id):
    auto = Auto.objects.get(id=auto_id)
    return render(request, 'ver_auto.html', {'auto': auto})

def actualizar_auto(request):
    ...
class ActualizarAuto(UpdateView):
    model = Auto
    template_name= 'actualizar_auto.html'
    #fields = {'marca', 'modelo'}
    fields = '__all__'