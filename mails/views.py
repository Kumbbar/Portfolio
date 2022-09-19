from .forms import MailForm
from django.shortcuts import render, redirect
from .services.telegram_bot import TelegramBotService


def send_message(request):
    if request.method == 'POST':
        form = MailForm(data=request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.save()
            TelegramBotService.send_message(
                new_message.name,
                new_message.contacts,
                new_message.text
            )
            return render(request, 'thanks.html', {'name': new_message.name, 'form': MailForm()})
    return redirect('main:index')
