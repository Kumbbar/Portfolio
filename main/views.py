from django.shortcuts import render
from mails.forms import MailForm


def index(request):
    form = MailForm()
    return render(request, 'index.html', {'form': form})
