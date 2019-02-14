from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blogdjango.apps.posts.models import Post

def details(request,slug):
    post = get_object_or_404(Post,slug=slug)
    posts = Post.objects.all()
    context = {
        'post':post,
        'posts':posts
    }
    template_name = 'posts/details.html'
    return render(request,template_name, context)

