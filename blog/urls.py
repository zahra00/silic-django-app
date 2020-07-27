from django.contrib import admin
from django.urls import path
from .views import index, json, template

urlpatterns = [
    path('', index, name="home"),
    path('json/', json, name="json"),
    path('home/', template, name="home"),

]