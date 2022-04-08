from django.contrib import admin
from django.urls import path

from artigos.views import home

urlpatterns = [
    path('', home),
]
