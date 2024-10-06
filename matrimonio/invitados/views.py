from django.shortcuts import render, redirect, get_object_or_404
from .forms import InvitadoForm
from .models import Invitado

def agregar_invitado(request):
    if request.method == 'POST':
        form = InvitadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_invitado')  # Redirige a la misma página después de guardar
    else:
        form = InvitadoForm()
    
    return render(request, 'invitados/agregar_invitado.html', {'form': form})


def lista_invitados(request):
    invitados = Invitado.objects.all()  # Obtiene todos los invitados
    return render(request, 'invitados/lista_invitados.html', {'invitados': invitados})


def eliminar_invitado(request, id):
    invitado = get_object_or_404(Invitado, id=id)  # Obtén el invitado por su ID
    if request.method == 'POST':
        invitado.delete()  # Elimina el invitado
        return redirect('lista_invitados')  # Redirige a la lista de invitados
    return render(request, 'invitados/eliminar_invitado.html', {'invitado': invitado})  # Confirma eliminación


def confirmar_asistencia(request, id):
    # Aquí puedes manejar la lógica para confirmar asistencia
    # Por ejemplo, podrías buscar al invitado por su ID y mostrar un formulario para confirmar su asistencia
    invitado = Invitado.objects.get(id=id)  # Obtener el invitado por su ID
    return render(request, 'invitados/confirmar_asistencia.html', {'invitado': invitado})
