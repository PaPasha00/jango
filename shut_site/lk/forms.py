from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import DateInput, TextInput, Textarea, TimeInput

from lk.models import Articles 

class AddTrainForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'date', 'time']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО'}),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'}),
            'time': TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Время'})
        }