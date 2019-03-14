from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from blogdjango.apps.posts.models import Post

User = get_user_model()

class RegisterForm(forms.ModelForm): #Herda de UserCreationForm
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    #Verifica se as digitadas são iguais
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação da senha está incorreta')
        return password2

    #Função para salvar o email no banco de dados
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1']) #set_password, criptografa a senha
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['image','name','username', 'email']

class EditAccountForm(forms.ModelForm): #ModelForm pega os campos do form

    def clean_email(self):
        email = self.cleaned_data['email']
        queryset =  User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('E-mail já cadastrado!')
        return email

    class Meta:
        model = User #Form que o modelForm vai pegar  os compos
        fields = ['name','username', 'email','image'] #Campos que serão importados

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','article','image','category',]