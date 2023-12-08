from django.urls import path
from . import views


urlpatterns = [
    path('lk', views.lk, name='lk'),
    path('add', views.add, name='add'),
    path('index_lk', views.index_lk, name='index_lk'),
    
]
