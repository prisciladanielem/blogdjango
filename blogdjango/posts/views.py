from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

from blogdjango.posts.forms import Contact

def home(request):
    posts = Post.objects.all()
    template_name = 'posts/home.html'
    context = {
        'posts':posts
    }
    return render(request,template_name,context)

def details(request,slug):
    post = get_object_or_404(Post,slug=slug)
    context = {
        'post':post
    }
    template_name = 'posts/details.html'
    return render(request,template_name, context)

def contact(request):
    template_name = 'contact.html'
    form = Contact()
    context = {'form' : form }
    return render(request, template_name, context)