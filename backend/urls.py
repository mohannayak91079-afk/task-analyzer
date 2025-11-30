
from django.urls import path, include
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', index),
    path('api/tasks/', include('tasks.urls')),
]
