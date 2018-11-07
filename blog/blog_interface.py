from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import UserForm


@login_required()
def add_blog(request):
    return render(request, 'blog/add_blog.html')

@login_required
def do_add_blog(request):
    title = request.POST.get('title')
    hcontent = request.POST.get('hcontent')
    this_user = User.objects.get(username=request.user.username)
    this_user.blog_set.create(title=title, content=hcontent)
    blog = Blog.objects.get(title=title)
    return redirect(f'/blog/{blog.blog_id}')

@login_required()
def edit_blog(request,blog_id):
    blog = Blog.objects.get(pk=blog_id)
    return render(request, 'blog/edit_blog.html' ,context={'blog':blog})

@login_required()
def do_edit_blog(request,blog_id):
    title = request.POST.get('title')
    hcontent = request.POST.get('hcontent')
    blog = Blog.objects.get(pk=blog_id)
    blog.title = title
    blog.content = hcontent
    blog.save()
    return redirect(f'/blog/{blog_id}')

@login_required()
def delete_blog(request,blog_id):
    Blog.objects.filter(pk=blog_id).delete()
    return redirect('index')

def get_blog(request,blog_id):
    #this_user = User.objects.get(username=request.user.username)
    info = Blog.objects.get(pk=blog_id)
    content = info.content.encode()
    return render(request, 'blog/blog.html', context={'info': info, 'content':content})