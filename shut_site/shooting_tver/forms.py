from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {'title': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя'
        }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите время'
            }),
        }
        


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'}),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail'}),
            'password1': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'}),
            'password2': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Повторите пароль'})
        }
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    
    

        