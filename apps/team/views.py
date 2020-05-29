from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Team
from .models import Student
from .forms import StudentForm

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

def team_details(request, idTeam):
    #Vista de registro de un alumno a un taller
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_details', idTeam)
        team = Team.objects.get(pk=idTeam)
        students = Student.objects.filter(idTeam = idTeam)
        return render(request, 'team_details.html', {'form':form, 'students':students, 'team':team})

    team = Team.objects.get(pk=idTeam)
    students = Student.objects.filter(idTeam = idTeam)
    form = StudentForm(initial = { 'idTeam' : idTeam })
    return render(request, 'team_details.html', {'form':form, 'students':students, 'team':team})
