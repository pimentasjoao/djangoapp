from django.shortcuts import render
from django.http import HttpResponse
from blog.dados import posts

# Create your views here.

def myblog(request):
    return HttpResponse("Ola blog")

def exemplo(request):
    context=posts
    return render(
        request,
        'index.html',
        {'texto': 'Ola Exemplo', 'titulo':'Exemplo', 'posts': context}
    )

def myblog2(request):
    return render(
        request,
        'index.html',
        {'texto': 'Ola utilizando templates html2', 'titulo':'Blog'}
    )