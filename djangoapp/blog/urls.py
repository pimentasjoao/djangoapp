
from django.urls import path
from . import views

#/blog
urlpatterns = [
   # path('', views.myblog),
    path('', views.myblog2,name='blog'),
    path('exemplo/', views.exemplo, name="exemplo"), #os nomes para as urls so serao usados para linkagem interna no site 
    path('exemplo/<int:postid>/', views.exemploid, name="exemploid"),
   
]
