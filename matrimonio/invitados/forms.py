from django import forms
from .models import Invitado

class InvitadoForm(forms.ModelForm):
    class Meta:
        model = Invitado
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion', 'asistira']
