from django.db import models

class PostManager(models.Manager):
    def search(self,query):
        return self.get_queryset().filter(models.Q(title__icontains=query) | models.Q(description__icontains=query))

class Post(models.Model):
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Atalho')
    article = models.TextField('Texto')
    categories = (
        ('sem categoria','sem categoria'),
        ('web design','web wesign'),
        ('photoshop','photoshop'),
        ('html5 e css3','html5 e css3'),
        ('web application','web application'),
        ('seo','seo')
    )
    category = models.CharField(max_length=20, choices=categories, default='sem categoria')
    image = models.ImageField(upload_to='posts/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = PostManager()

    @models.permalink
    def get_absolute_url(self):
        return('details',(),({'slug':self.slug}))
