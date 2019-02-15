from django.urls import path
from django.contrib.auth.views import LoginView
from blogdjango.apps.accounts.views import register

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html') , name='login' ),
    path('cadastre-se/', register, name="register"),
]
