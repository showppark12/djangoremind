from django.shortcuts import render, redirect,get_object_or_404
from .models import FormBlog
from .forms import FormBlogForm
# Create your views here.

def FormBlogMain(request):
    blog = FormBlog.objects.all
    return render(request, 'fblogmain.html', {"blogs":blog})

def FormBlogDetail(request, blog_id):
    blog_detail = get_object_or_404(FormBlog, pk=blog_id)
    return render(request, 'fblogdetail.html',{'blog': blog_detail })

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
        return redirect('/formblog/'+str(blog_id))
    else:
        form = FormBlogForm(instance= update_blog)

    return render(request, 'fblogupdate.html', {'form':form})


def FormBlogDelete(request, blog_id):
    delete_blog = FormBlog.objects.get(id = blog_id)
    delete_blog.delete()
    return redirect('/formblog/main')