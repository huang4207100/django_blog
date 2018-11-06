from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Blog
# Create your views here.


def index(request):
    return render(request, 'blog/index.html', context=None)

def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'blog/login.html',context=None)
    else:
        return Http404('登录失败,请检查账号和密码')

def user_logout(request):
    logout(request)
    return render(request,'blog/logout.html', context=None)

@login_required(login_url='blog/index/')
def add_blog(request,blog_id):
    pass 

@login_required(login_url='blog/index/')
def edit_blog(request,blog_id):
    pass

@login_required(login_url='blog/index/')
def delete_blog(request,blog_id):
    pass

#@login_required(login_url='blog/index/')
def get_blog(request,blog_id):
    return render(request, 'blog/blog.html', context=None)
