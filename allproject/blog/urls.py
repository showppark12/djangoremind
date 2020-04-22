from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main', views.BlogMain, name = 'blogmain'),
    path('<int:blog_id>', views.BlogDetail, name = 'blogdetail'),
    path('create', views.BlogCreate, name = 'blogcreate'),
    path('new', views.BlogNew, name ='blognew'),
    path('edit/<int:blog_id>', views.BlogEdit, name='blogedit'),
    path('update/<int:blog_id>', views.BlogUpdate, name= 'blogupdate'),
    path('delete/<int:blog_id>', views.BlogDelete, name= 'blogdelete'),
]