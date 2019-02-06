from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display= ['title', 'slug', 'created_at']
    search_fields = ['title','slug'] #Exibe uma barra de pesquisa, onde é possível pesquisar por esses campos
    prepopulated_fields ={'slug':('title',)}

admin.site.register(Post, PostAdmin)

