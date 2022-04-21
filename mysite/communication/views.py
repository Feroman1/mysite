from django.shortcuts import render, redirect
from .models import mail
from .forms import mailForm

def mail(request):
    error = ''
    if request.method =="POST":
        form=mailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверные данные'
    form = mailForm()
    data = {'form': form, 'error': error}
    return render(request, 'communication/mail.html', data)
# Create your views here.
