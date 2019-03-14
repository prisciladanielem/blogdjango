from django.urls import path
from blogdjango.apps.posts.views import details, new_post, show_posts

urlpatterns = [
    path('novo-post/', new_post, name="new_post"),
    path('meus-posts/', show_posts, name="show_posts"),
    path('<str:slug>/', details, name="details"),
]