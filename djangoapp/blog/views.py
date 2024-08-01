from django.shortcuts import render
from django.http import HttpResponse
from blog.dados import posts

# Create your views here.

def myblog(request):
    return HttpResponse("Ola blog")

def myblog2(request):
    return render(
        request,
        'index.html',
        {'texto': 'Ola utilizando templates html2', 'titulo':'Blog'}
    )

def exemplo(request):
    context=posts
    return render(
        request,
        'index.html',
        {'texto': 'Ola Exemplo', 'titulo':'Exemplo', 'posts': context}
    )

def exemploid(request, id):
    res=posts
    context=None
    for post in res:
        if post['id'] == id:
            context=post

    return render(
        request,
        'index2.html',
        {'texto': 'Ola Exemplo', 'titulo':'Exemplo', 'posts': context}
    )
