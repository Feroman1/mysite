from .models import mail
from django.forms import ModelForm, TextInput, Textarea

class mailForm(ModelForm):
    class Meta:
        model = mail
        fields = ['email', 'number', 'message']
        widgets = {'email': TextInput(attrs={'placeholder': "E-mail", 'class': "form-control"}),
                   'number': TextInput(attrs={'placeholder': "Номер для связи", 'class': "form-control"}),
                   'message': Textarea(attrs={'placeholder': "Сообщение", 'class': "form-control"})
                   }