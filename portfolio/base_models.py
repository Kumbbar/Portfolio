from django.db import models


class Base(models.Model):
    class Meta:
        abstract = True

    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    date = models.DateField(null=True)
