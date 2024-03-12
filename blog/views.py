from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'blog/index.html',{'nome':'JOAO'})

def create(request):
    return render(request,'blog/blog.html',{'nome':'JOAO'})