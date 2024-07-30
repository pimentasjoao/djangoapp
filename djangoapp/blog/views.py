from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myblog(request):
    return HttpResponse("Ola blog")

def exemplo(request):
    return HttpResponse("Ola exemplo do blog")

def myblog2(request):
    return render(
        request,'index.html'
    )