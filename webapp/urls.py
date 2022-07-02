from django.contrib import admin
from django.urls import path

from webapp.views import index_view, create_article, delete_article, update_article

urlpatterns = [
    path("", index_view, name="index"),
    path("article/add/", create_article, name="create_article"),
    path('article/<int:pk>/update', update_article, name="update_article"),
    path('article/<int:pk>/delete', delete_article, name="delete_article"),
]
