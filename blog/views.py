from django.shortcuts import render, HttpResponse

from .models import Post

# Create your views here.
def posts(request):
    first_post=Post.objects.first()#Obtenemos el primer elemtno de la base de datos
    posts = Post.objects.all()#obtenemos los datos de la base de datos
    return render(request,'blogs.html', {'posts':posts, 'first_post':first_post})#enviamos un dictionario

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog.html', {'post':post})

