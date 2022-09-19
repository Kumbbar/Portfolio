from portfolio.base_models import Base
from django.db import models
from portfolio.settings import BASE_DIR
import os


class Event(Base):
    image = models.ImageField(upload_to=os.path.join(BASE_DIR, 'static/img/events/'))

    class Meta:
        db_table = 'events'
