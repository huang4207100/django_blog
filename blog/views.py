from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse,Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import UserForm
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')

def register(request):
    return render(request, 'blog/register.html')

def do_register(request):
    form = UserForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['your_name']
        password = form.cleaned_data['password']
        queryset = User.objects.filter(username=username)
        if queryset.exists():
            return render(request, 'blog/register.html',context={"error":f'用户{username}已注册，请换个账号重新注册'})
        new_user = User.objects.create_user(username,password=password)
        new_user.save()
    return redirect('login')
    

def user_login(request):
     return render(request, 'blog/login.html')

def do_user_login(request):
    #username = request.POST['username']
    #password = request.POST['password']
    form = UserForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['your_name']
        password = form.cleaned_data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'blog/login.html',context={"error":f'用户{username}无法登陆，请检查账号或密码'})

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required()
def add_blog(request):
    return render(request, 'blog/add_blog.html')

@login_required
def do_add_blog(request):
    title = request.POST.get('title')
    hcontent = request.POST.get('hcontent')
    this_user = User.objects.get(username=request.user.username)
    this_user.blog_set.create(title=title, content=hcontent)
    print(666)
    return render(request, 'blog/index.html')

#@login_required(login_url='blog/index/')
def edit_blog(request,blog_id):
    pass

#@login_required(login_url='blog/index/')
def delete_blog(request,blog_id):
    pass

#@login_required(login_url='blog/index/')
def get_blog(request,blog_id):
    this_user = User.objects.get(username=request.user.username)
    info = this_user.blog_set.get(pk=blog_id)
    content = info.content.encode()
    return render(request, 'blog/blog.html', context={'info': info, 'content':content})
