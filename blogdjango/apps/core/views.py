from django.shortcuts import render
from django.core.paginator import Paginator

from blogdjango.apps.posts.models import Post
from blogdjango.apps.posts.forms import Contact

def base(request):
    posts_recents = Post.objects.all()
    template_name = 'base.html'
    context = {
        'posts_recents':posts_recents
    }
    return render(request,template_name,context)

def home(request):
    posts_list = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    template_name = 'posts/home.html'
    context = {
        'posts':posts,
    }
    return render(request,template_name,context)

def contact(request):
    posts = Post.objects.all()
    template_name = 'contact.html'
    form = Contact()
    context = {
        'form' : form,
        'posts' : posts 
                }
    return render(request, template_name, context)
