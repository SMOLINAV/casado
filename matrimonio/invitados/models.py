from django.db import models

class Invitado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    asistira = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
