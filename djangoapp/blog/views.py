from django.shortcuts import render
from django.http import HttpResponse, Http404
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

def exemploid(request, postid):
    found_post = None
    for post in posts:
        if post['id'] == postid:
            found_post=post
            break
    if found_post==None:
        raise Http404("Item nao existe")
    return render(
        request,
        'index2.html',
        {'texto': 'Ola Exemplo', 'titulo':'Exemplo', 'posts': found_post}
    )
