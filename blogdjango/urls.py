from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blogadmindjango/', admin.site.urls),
    path('', include('blogdjango.apps.core.urls')),
    path('posts/', include('blogdjango.apps.posts.urls')),
    path('conta/', include('blogdjango.apps.accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)