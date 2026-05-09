from django.shortcuts import render
from .checker import run_checker
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):

    form = AuthenticationForm()

    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()
            login(request, user)

            return redirect('/kaysfinalproject/checker/')

    return render(request, 'medications/home.html', {'form': form})


@login_required
def checker_view(request):
    if request.method == 'POST':
        symptom_check = request.POST.get('symptom_check')
        med2 = request.POST.get('med2')
        result = run_checker(med2)
        return render(request, 'medications/checker.html', {'result': result})
    return render(request, 'medications/checker.html')

def home(request):
    return render(request, 'medications/home.html')

