from django import template

from blogdjango.apps.posts.models import Post

register = template.Library() #Para ser uma biblioteca de tags válida, o módulo deve conter uma variável do nível do módulo chamado register que é uma instância de template.Library, na qual todas as tags e filtros são registrados. 

@register.inclusion_tag('templatetags/posts_recents.html') #Converte essa função em uma tag que pode ser usada pelo django e retorna um template
def postagens_recentes(self):
    posts = Post.objects.all() #Pega as inscrições de um usuário
    context = {
        'posts': posts
    }
    return context