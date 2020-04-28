from django import forms
from .models import FormBlog

class FormBlogForm(forms.ModelForm):
    class Meta:
        model = FormBlog
        fields = ['title','body']