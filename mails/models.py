from django.db import models


class Mail(models.Model):
    name = models.CharField(max_length=100, null=True)
    contacts = models.CharField(max_length=200, null=True)
    text = models.TextField(max_length=800, null=True)

    class Meta:
        db_table = 'mails'
