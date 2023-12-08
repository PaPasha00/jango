from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shooting_tver.urls')),
    path('', include('lk.urls'))
]
