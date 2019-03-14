from django.db import models
from django.conf import settings
from django.utils.text import slugify

class PostManager(models.Manager):
    def search(self,query):
        return self.get_queryset().filter(models.Q(title__icontains=query) | models.Q(description__icontains=query))

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             verbose_name='Usuário',
                             on_delete=models.CASCADE
                            )
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Atalho')
    article = models.TextField('Texto')
    categories = (
        ('sem categoria','sem categoria'),
        ('poema','poema'),
        ('poesia','poesia'),
        ('haikai','haikai')
    )
    category = models.CharField('Categoria',max_length=20, choices=categories, default='sem categoria')
    image = models.ImageField(upload_to='posts/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = PostManager()

    @models.permalink
    def get_absolute_url(self):
        return('details',(),({'slug':self.slug}))

    class Meta:
        ordering = ['-created_at']

    #Preenche o slug automático quando o post é adicionado por dentro do sistema
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Post, self).save(*args, **kwargs)