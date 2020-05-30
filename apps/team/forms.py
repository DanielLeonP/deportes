from django import forms
from .models import Student, Team

class StudentForm(forms.ModelForm):
    #Formulario para registrar alumnos

    class Meta:
        model = Student
        exclude = ('liberado',)
        labels = {
            'idTeam':'' #No mostrar
        }
        widgets = {
            'idTeam':forms.NumberInput(attrs={'hidden':True})
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'