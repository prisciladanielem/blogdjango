from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from blogdjango.apps.posts.models import Post
from blogdjango.apps.accounts.forms import PostForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

def details(request,slug):
    post = get_object_or_404(Post,slug=slug)
    posts = Post.objects.all()
    context = {
        'post':post,
        'posts':posts
    }
    template_name = 'posts/details.html'
    return render(request, template_name, context)


def new_post(request):
    # user,a = Post.objects.get_or_create(user=request.user)
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Post criado com sucesso!')
            return redirect('dashboard')
    else:
        form = PostForm(instance=request.user)
    template_name = 'posts/new_post.html'
    context['form'] = form
    return render (request, template_name, context)

def show_posts(request):
    posts = Post.objects.filter(user=request.user)
    context = {
        'posts': posts
    }
    template_name = 'posts/show_posts.html'
    return render(request, template_name, context)