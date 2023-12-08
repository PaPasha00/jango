from django.urls import path
from django.contrib import admin
from . import views
from django.urls import path
from django.conf import settings

urlpatterns = [
    path('', views.first_page, name='home'),
    path('first_page', views.first_page, name='first_page'),
    path('about', views.about, name='about'),
    path('create', views.RegisterUser.as_view(), name='create'),
    path('admin', admin.site.urls),
    path('login', views.LoginUser.as_view(), name='login'),
    path('index', views.index, name='index'),
    
]
