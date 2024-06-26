from django.urls import path
from .views import index, install

urlpatterns = [
    path('', index, name='index'),
    path('install', install, name='install')
]
