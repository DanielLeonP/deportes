from django.urls import path
from . import views

urlpatterns = [
    path('equipos/', views.equipos, name="equipos"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('estudiantes/plan/<str:plan>/', views.estudiantes_plan, name="estudiantesByPlan"),
    path('estudiantes/equipo/<int:idTeam>/', views.estudiantes_equipo, name="estudiantesByTeam"),
    path('team_details/<int:idTeam>/', views.team_details, name="team_details"),
    path('edit_team/<int:idTeam>/', views.edit_team, name="edit_team"),
]