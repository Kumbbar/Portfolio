from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('all/', views.get_all_projects_page, name='get_all_projects_page'),
    path('<str:title>/', views.get_project_page, name='get_project_page')
]