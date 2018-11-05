from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Blog
# Create your views here.
def login(request):
    return JsonResponse({'msg':True})