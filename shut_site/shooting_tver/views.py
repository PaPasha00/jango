from django.shortcuts import render
from .models import Task
from .utils import DataMixin
from .forms import LoginUserForm, RegisterUserForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

def first_page(request):
    return render(request, 'shooting_tver/first_page.html')

def index(request):
    tasks = Task.objects.all()
    return render(request, 'shooting_tver/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'shooting_tver/about.html')


def create(request):
    return render(request, 'shooting_tver/create.html')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shooting_tver/create.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items())+list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('login')
    

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shooting_tver/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items())+ list(c_def.items()))    
    
    def get_success_url(self):
        return reverse_lazy('lk')