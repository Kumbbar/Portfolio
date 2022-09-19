from django import forms
from projects.models import Project
from .models import Mail
from projects.models import Project


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ['name', 'contacts', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}),
            'contacts': forms.TextInput(attrs={'placeholder': 'Контакты',  'class': 'form-control'}),
            'text': forms.Textarea(
                attrs={'placeholder': 'Сообщение', 'class': 'form-control'}
            ),
        }


