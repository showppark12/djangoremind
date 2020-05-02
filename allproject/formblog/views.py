from django.shortcuts import render, redirect,get_object_or_404
from .models import FormBlog
from .forms import FormBlogForm
from .models import Comment
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.

def FormBlogMain(request):
    blog = FormBlog.objects.all
    return render(request, 'fblogmain.html', {"blogs":blog})

def FormBlogDetail(request, blog_id):
    blog_detail = get_object_or_404(FormBlog, pk=blog_id)
    comments= blog_detail.comments.all()
    return render(request, 'fblogdetail.html',{'blog': blog_detail , 'comments': comments})

def FormBlogCreate(request):
    if request.method == 'POST':
        form = FormBlogForm(request.POST )
        if form.is_valid():
            blog = form.save()
            blog.save()
            return redirect('fblogmain')
    else:
        form = FormBlogForm()
        return render(request, 'fblogcreate.html',{'form':form})

def FormBlogUpdate(request, blog_id):
    update_blog = FormBlog.objects.get(id=blog_id)
    if request.method == 'POST':
        form = FormBlogForm(request.POST, instance= update_blog)
        if form.is_valid():
            form.save()
        return redirect('fblogdetail',blog_id)
    else:
        form = FormBlogForm(instance= update_blog)

    return render(request, 'fblogupdate.html', {'form':form})


def FormBlogDelete(request, blog_id):
    delete_blog = FormBlog.objects.get(id = blog_id)
    delete_blog.delete()
    return redirect('fblogmain')

def CommentCreate(request, blog_id):
    if request.method == 'POST':
        new_comment = Comment()
        user = request.user
        new_comment.writer = get_object_or_404(User, username = user)
        new_comment.blog = get_object_or_404(FormBlog,pk = blog_id)
        new_comment.created = timezone.datetime.now()
        new_comment.text = request.POST['Ctext']
        new_comment.save()
    return redirect('fblogdetail', blog_id)