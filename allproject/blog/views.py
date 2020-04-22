from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog
from django.utils import timezone


def BlogMain(request):
    blogs= Blog.objects.all()
    return render(request, 'blogmain.html', {'blogs':blogs})

def BlogDetail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogdetail.html',{'blog': blog_detail })

def BlogNew(request):
    return render(request, 'blogcreate.html')

def BlogCreate(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.date = timezone.datetime.now()
    new_blog.body = request.POST['body']
    new_blog.save()
    return redirect('/blog/'+str(new_blog.id))

def BlogEdit(request, blog_id):
    edit_blog = Blog.objects.get(id=blog_id)
    return render(request,'blogedit.html',{'blog':edit_blog})

def BlogUpdate(request, blog_id):
    update_blog = Blog.objects.get(id=blog_id)
    update_blog.title = request.POST['title']
    update_blog.body = request.POST['body']
    update_blog.date = timezone.datetime.now()
    update_blog.save()
    return redirect('/blog/'+str(blog_id))

def BlogDelete(request, blog_id):
    delete_blog = Blog.objects.get(id = blog_id)
    delete_blog.delete()
    return redirect('/blog/main')