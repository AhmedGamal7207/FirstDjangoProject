from django.contrib import admin
from django.urls import path
from FirstApp.views import MyHome,MyAbout

urlpatterns = [
    path('home/', MyHome, name="home"),
    path('', MyHome, name="home"),
    path('about/', MyAbout, name="about"),
]