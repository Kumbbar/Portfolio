from django.shortcuts import render
from .services.projects import ProjectsService
from mails.forms import MailForm


def get_all_projects_page(request):
    form = MailForm()
    projects = ProjectsService.get_all()
    return render(request, 'projects.html', {'projects': projects, 'form': form})


def get_project_page(request, title: str):
    form = MailForm()
    project = ProjectsService.get_by_title(title)
    return render(request, 'project.html', {'project': project, 'form': form})
