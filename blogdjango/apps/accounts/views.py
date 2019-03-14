from django.shortcuts import render, redirect
from blogdjango.apps.accounts.forms import RegisterForm, EditAccountForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib import messages

from django.contrib.auth.decorators import login_required

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save() #salva os dados no banco de dados
            user = authenticate(username = user.username, password = form.cleaned_data['password1'])
            login(request,user) #loga o usuário após se cadastrar no sistema
            return redirect('/') # redireciona para essa página após o login
    else:
        form =  RegisterForm()
    context = {
    'form':form
    }
    template_name = 'accounts/register.html'
    return render(request, template_name, context)

@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    context = {}
    return render(request, template_name, context)

@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, request.FILES, instance=request.user) #O request.FILES faz o upload das imagens
        if form.is_valid():
            form.save()
            messages.success(request, 'Dados alterados com sucesso!')
            return redirect('dashboard')
    else:
        form = EditAccountForm(instance=request.user) # se não for post, formulaŕio vazio
    context['form'] = form
    return render(request, template_name, context) 