
from django.urls import path
from . import views

#/blog
urlpatterns = [
   # path('', views.myblog),
    path('', views.myblog2),
    path('exemplo/', views.exemplo),
   
]
