from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core.validators import RegexValidator

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField('Usuário',
                                max_length=30,
                                unique=True,
                                validators=[RegexValidator(r'^[\w.@+-]+$', #Valida se existe catacter inválido no nome de usuário
                                message='O nome de usuário pode ser somente letras, números e os caracteres @/ ./ -/ _/',
                                code='invalid')])
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    image = models.ImageField(upload_to='accounts/images', verbose_name='Imagem', null=True, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    data_joined = models.DateTimeField('Data de entrada',auto_now_add=True)
 
    objects = UserManager()
 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
 
    def __str__(self):
        return self.name or self.username
 
    def get_short_name(self):
        return self.username
 
    def get_full_name(self):
        return str(self)
 
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
