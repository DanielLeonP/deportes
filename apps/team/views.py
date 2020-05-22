from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
from .models import Student
# Create your views here.
def equipos(request):
    #Todos los equipos
    equipos=Team.objects.all()
    print("*************")
    print(equipos)
    print("*************")
    return HttpResponse(equipos)

def estudiantes(request):
    #Todos los estudiantes
    estudiantes = Student.objects.all()
    print("*************")
    print(estudiantes)
    print("*************")
    return HttpResponse(estudiantes)

def estudiantes_plan(request, plan):
    #Todos los estudiantes por plan
    estudiantes = Student.objects.filter(plan = plan)
    print("*************")
    print(estudiantes)
    print("*************")
    return HttpResponse(estudiantes)

def estudiantes_equipo(request, idTeam):
    #Todos los estudiantes por plan
    estudiantes = Student.objects.filter(idTeam = idTeam)
    print("*************")
    print(estudiantes)
    print("*************")
    return HttpResponse(estudiantes)