from django.db import models

class Prospect(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    telefono = models.CharField(max_length=30, blank=True)
    estatus = models.CharField(max_length=50, default='Nuevo')
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Seguimiento(models.Model):
    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE, related_name='seguimientos')
    fecha = models.DateTimeField(auto_now_add=True)
    nota = models.TextField()
    creado_por = models.CharField(max_length=100, blank=True)
    nuevo_estatus = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Seguimiento de {self.prospect.nombre}"
