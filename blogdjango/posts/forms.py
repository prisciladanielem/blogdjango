from django import forms

class Contact(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    last_name = forms.CharField(label='Sobrenome', max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label='Assunto', max_length=80)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)