from django.shortcuts import render
from blog.models import Categoria, Post, Categoria

# Create your views here.

def blog(request):

    posts=Post.objects.all() 
    return render(request, "blog/blog.html", {'posts':posts})


def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria_id)
    return render(request, "blog/categorias.html", {'categoria':categoria, 'posts':posts})