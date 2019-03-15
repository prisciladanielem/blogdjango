from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from blogdjango.apps.accounts.views import register,dashboard, edit, edit_password

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('login/', LoginView.as_view(template_name='accounts/login.html') , name='login' ),
    path('sair/', LogoutView.as_view(next_page='/') , name='logout' ),
    path('editar-dados/', edit, name='edit' ),
    path('alterar-senha/', edit_password, name='edit_password'),
    path('cadastre-se/', register, name="register"),
]
