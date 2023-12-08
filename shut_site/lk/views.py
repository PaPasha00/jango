from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .forms import AddTrainForm
from shooting_tver.utils import DataMixin
from .models import Articles

def lk(request):
    lk = Articles.objects.order_by('date', 'time')
    return render(request, 'lk/lk.html', {'lk': lk})

def add(request):
    error = ''
    if request.method == 'POST':
        form = AddTrainForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lk')
        else:
            error = 'Форма неверна'
    

    form = AddTrainForm()
    data = {'form': form}
    return render(request, 'lk/add.html', data)

def index_lk(request):
    return render(request, 'lk/index_lk.html')