from django.contrib import admin
from django.urls import path
from simulation.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
]