from django.contrib import admin
from .models import FormBlog
from .models import Comment
# Register your models here.

admin.site.register(FormBlog)
admin.site.register(Comment)
