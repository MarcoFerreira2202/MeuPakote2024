from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import Sign_upForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = Sign_upForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            form = Sign_upForm()
    else:
        form = Sign_upForm()
    return render(request, 'sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # loga o usuário
            user = form.get_user()
            login(request, user)
            return redirect('index')
        else:
            form = AuthenticationForm()
            return render(request, 'login.html', {'form': form, 'error_message': 'Usuário ou senha inválidos'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})