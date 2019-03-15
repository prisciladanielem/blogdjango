from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from blogdjango.apps.posts.models import Post
from blogdjango.apps.accounts.forms import PostForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

from django.core.paginator import Paginator

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

@login_required
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
        form = PostForm()
    template_name = 'posts/new_post.html'
    context['form'] = form
    return render (request, template_name, context)

@login_required
def edit_post(request,slug):
    post = get_object_or_404(Post,slug=slug)
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post) #O request.FILES faz o upload das imagens
        if form.is_valid():
            form.save()
            messages.success(request,'Post alterado com sucesso!')
            return redirect('dashboard')
    else:
        form = PostForm(instance=post) # se não for post, formulaŕio vazio
    context['form'] = form
    template_name = 'posts/edit_post.html'
    return render(request, template_name, context)

@login_required
def delete_post(request,slug):
    post = get_object_or_404(Post,slug=slug,user = request.user) 
    if request.method=='POST': # Testa se o usuário quer cancelar a inscrição
        post.delete() # deleta a inscrição
        messages.success(request,'Post excluído com sucesso!')
        return redirect('dashboard')
    context = {
        'post': post,
    }
    template_name = 'posts/delete_post.html'
    return render(request, template_name, context)

@login_required
def show_posts(request):
    posts_list = Post.objects.filter(user=request.user)
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts
    }
    template_name = 'posts/show_posts.html'
    return render(request, template_name, context)