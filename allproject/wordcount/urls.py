from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main', views.wcmain, name='wcmain'),
    path('result', views.result, name= 'result'),
]