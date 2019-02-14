from django.shortcuts import render
from blogdjango.apps.posts.models import Post

from blogdjango.apps.posts.forms import Contact

def base(request):
    posts = Post.objects.all()
    template_name = 'base.html'
    context = {
        'posts':posts
    }
    return render(request,template_name,context)

def home(request):
    posts = Post.objects.all()
    template_name = 'posts/home.html'
    context = {
        'posts':posts
    }
    return render(request,template_name,context)

def contact(request):
    posts = Post.objects.all()
    template_name = 'contact.html'
    form = Contact()
    context = {
        'form' : form,
        'posts':posts 
                }
    return render(request, template_name, context)
