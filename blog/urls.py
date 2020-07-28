from django.contrib import admin
from django.urls import path
from .views import index, json, template, list_all_article, detail_article

app_name = "blog"
urlpatterns = [
    path('', index, name="home"),
    path('json/', json, name="json"),
    path('home/', list_all_article, name="home"),
    path('test/', template, name="home"),
    path('article/<slug:slug>', detail_article, name="detail")

]