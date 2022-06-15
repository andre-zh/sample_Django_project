from django.urls import path
from . import views

urlpatterns = [
    path('simple_vie', views.simple, name='simple') # first_app --> PROJECT urls.py
]