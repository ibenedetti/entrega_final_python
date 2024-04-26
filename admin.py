from django.contrib import admin
from myapp.models import Estudiante, Profesor, Examen

admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Examen)