from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from usuarios.models import Usuario


# Create your views here.
def list_usuarios(request):

    contexto = {
        'usuarios': Usuario.objects.all(),
    }

    return render(request, 'usuarios/lista.html',contexto)

def add_usuarios(request):

    if request.method == 'GET':
        return render(request, 'usuarios/formulario.html')
    
    if request.method == "POST":
        print(request.POST)

        Usuario.objects.create(
            nombre = request.POST['nombre'],
            apellido = request.POST['apellido'],
            username = request.POST['username'],
            email = request.POST['email'],
            password = request.POST['password'],
        )
    
    return redirect(reverse('usuarios:listado'))


def edit_usuarios(request, id):
    
    usuario = Usuario.objects.get(id=id)

    if request.method == 'GET':

        contexto = {
            'usuario' : usuario
        }

        return render(request, 'usuarios/formulario_editar.html',contexto)
    
    if request.method == "POST":
        print(request.POST)

        usuario.nombre = request.POST['nombre']
        usuario.apellido = request.POST['apellido']
        usuario.username = request.POST['username']
        usuario.email = request.POST['email']  
        usuario.save()

        
    return redirect(reverse('usuarios:listado'))


def delete_usuarios(request, id):
    
    usuario = Usuario.objects.get(id=id)
    
    if request.method == "GET":
        contexto = {
            'usuario' : usuario
        }

        return render(request, 'usuarios/delete.html',contexto)

    if request.method == "POST":

        usuario.delete()
        
    return redirect(reverse('usuarios:listado'))

def delete_usuarios_api(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return JsonResponse({ 'success': True })