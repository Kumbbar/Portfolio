from ..models import Project
from typing import List


class ProjectsService:

    @classmethod
    def get_all(cls) -> List[Project]:
        projects = Project.objects.order_by('-date')
        for project in projects:
            project.image = str(project.image)[7:]
            project.description = project.description[:100] + '...'
        return projects

    @classmethod
    def get_by_title(cls, title: str) -> Project:
        project = Project.objects.get(title=title)
        project.image = str(project.image)[7:]
        return project

