from django.shortcuts import render, redirect
from blogdjango.apps.accounts.forms import RegisterForm
from django.contrib.auth import authenticate, login

def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
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
    return render(request, template_name,context)