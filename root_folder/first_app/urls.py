from django.urls import path
from . import views

urlpatterns = [
    path('simple_view', views.simple, name='simple'), # first_app --> PROJECT urls.py
    path('new_example', views.temp)
]