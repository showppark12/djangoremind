from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('main', views.FormBlogMain, name = 'fblogmain'),
    path('detail/<int:blog_id>', views.FormBlogDetail, name = 'fblogdetail'),
    path('create', views.FormBlogCreate, name = 'fblogcreate'),
    path('update/<int:blog_id>', views.FormBlogUpdate, name= 'fblogupdate'),
    path('delete/<int:blog_id>', views.FormBlogDelete, name= 'fblogdelete'),
    path('newcomment/<int:blog_id>', views.CommentCreate, name='ccreate'),
]