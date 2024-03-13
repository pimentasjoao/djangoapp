from django.http import HttpResponse
from django.shortcuts import render
from blog.data import post

# Create your views here.
context= {'posts': post}


def home(request):
    return render(request,'blog/index.html',context)

def create(request):
    return render(request,'blog/blog.html',context)