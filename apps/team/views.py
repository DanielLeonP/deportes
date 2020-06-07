from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Team
from .models import Student
from .forms import StudentForm, TeamForm

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

@login_required
def team_details(request, idTeam):
    #Vista de registro de un alumno a un taller
    #team = Team.objects.get(pk=idTeam)
    team = get_object_or_404(Team, pk = idTeam)
    students = Student.objects.filter(idTeam = idTeam)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        total_students = Student.objects.filter(idTeam = idTeam).count()
        if total_students < team.max_students:            
            if form.is_valid():
                form.save()
                messages.success(request,'Listo!')       
                return redirect('team_details', idTeam) 
            return render(request, 'team_details.html', {'form':form, 'students':students, 'team':team})
        else:
            messages.error(request, 'Cupo lleno')
            return render(request, 'team_details.html', {'form':form, 'students':students, 'team':team})
    #team = Team.objects.get(pk=idTeam)
    form = StudentForm(initial = { 'idTeam' : idTeam })
    return render(request, 'team_details.html', {'form':form, 'students':students, 'team':team})

@login_required
def edit_team(request, idTeam):        
    #team = Team.objects.get(pk = idTeam)
    team = get_object_or_404(Team, pk = idTeam)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance =team)
        if form.is_valid():
            if form.has_changed():
                form.save()
                messages.success(request, 'Listo!')
        else:
            messages.error(request, 'Faltan datos')
    form = TeamForm(instance = team)
    return render(request, 'edit_team.html', {'form': form })

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    idTeam = student.idTeam.id
    student.delete()
    return redirect('team_details', idTeam)

@login_required
def liberar_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.liberado = True
    idTeam = student.idTeam.id
    student.save()
    return redirect('team_details', idTeam)

@login_required
@user_passes_test(lambda u: u.is_superuser, login_url='panel')
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Listo')
        else:
            messages.error(request, 'No se pudo registrar, revisa tus datos')
    form = TeamForm()
    return render(request, 'create_team.html', {'form':form})