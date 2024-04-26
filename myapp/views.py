from django.shortcuts import render, redirect
from .forms import EstudianteForm, ProfesorForm, ExamenForm
from django.core.serializers.json import DjangoJSONEncoder

import json

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()  
            nuevo_estudiante = form.instance

            datos_estudiante = {
                'id': nuevo_estudiante.id,
                'nombre': nuevo_estudiante.nombre,
                'apellido': nuevo_estudiante.apellido,
                'email': nuevo_estudiante.email,
                'fecha_inscripcion': nuevo_estudiante.fecha_inscripcion.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            
            with open('datos_estudiantes.json', 'a') as f:
                json.dump(datos_estudiante, f)
                f.write('\n')  
            
            return redirect('inicio')  
    else:
        form = EstudianteForm()
    return render(request, 'agregar_estudiante.html', {'form': form})


def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()  
            nuevo_profesor = form.instance

            datos_profesor = {
                'id': nuevo_profesor.id,
                'nombre': nuevo_profesor.nombre,
                'apellido': nuevo_profesor.apellido,
                'email': nuevo_profesor.email
            }
                        
            
            with open('datos_profesores.json', 'a') as f:
                json.dump(datos_profesor, f)
                f.write('\n') 


            return redirect('inicio') 
    else:
        form = ProfesorForm()
    return render(request, 'agregar_profesor.html', {'form': form})

def agregar_examen(request):
    if request.method == 'POST':
        form = ExamenForm(request.POST)
        if form.is_valid():
            nuevo_examen = form.save(commit=False)
            nuevo_examen.save()

            datos_examen = {
                'asignatura': nuevo_examen.asignatura,
                'fecha': nuevo_examen.fecha,
                'hora': nuevo_examen.hora,
                'fecha_creacion': nuevo_examen.fecha_creacion
            }
            
            with open('datos_examenes.json', 'a') as f:
                json.dump(datos_examen, f, cls=DjangoJSONEncoder)
                f.write('\n')

            return redirect('inicio')
    else:
        form = ExamenForm()
    return render(request, 'agregar_examen.html', {'form': form})


def inicio(request):
    return render(request, 'inicio.html')
