from django.db import models
from portfolio.base_models import Base
from portfolio.settings import BASE_DIR
import os


class Project(Base):
    technologies = models.TextField(null=True)
    image = models.ImageField(upload_to=os.path.join(BASE_DIR, 'static/img/projects/'), null=True)

    class Meta:
        db_table = 'projects'


