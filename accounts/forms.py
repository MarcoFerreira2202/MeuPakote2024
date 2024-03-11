from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Sign_upForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username': 'Usuário', 'email': 'E-mail','password1': 'Senha', 'password2': 'Confirmação de senha'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control'}),
                    'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
                    'password2': forms.PasswordInput(attrs={'class': 'form-control'})}