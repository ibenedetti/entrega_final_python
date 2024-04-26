from django.db import models
from django.utils import timezone

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Examen(models.Model):
    asignatura = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Examen de {self.asignatura} - {self.fecha} - {self.hora}"
