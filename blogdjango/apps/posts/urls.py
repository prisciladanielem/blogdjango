from django.urls import path
from blogdjango.apps.posts.views import details

urlpatterns = [
    path('<str:slug>/', details, name="details"),
]