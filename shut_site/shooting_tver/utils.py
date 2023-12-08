from django.db.models import Count

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        el = Task.objects.all()
        context['menu'] = menu
        context['el'] = el
        if 'el_selected' not in context:
            context['el_selected'] = 0
        return context