from django.urls import path
from blogdjango.apps.posts.views import details, new_post, edit_post, delete_post, show_posts

urlpatterns = [
    path('novo-post/', new_post, name="new_post"),
    path('excluir-post/<str:slug>/', delete_post, name="delete_post"),
    path('editar-post/<str:slug>/', edit_post, name="edit_post"),
    path('meus-posts/', show_posts, name="show_posts"),
    path('<str:slug>/', details, name="details"),
]