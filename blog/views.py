from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def blog(request):
    return HttpResponse('Olá Blog')

def exemplo(request):
    return render(request,'blog/index.html',{'nome':'JOAO'})