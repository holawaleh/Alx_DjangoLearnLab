from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),      # Homepage
    path("posts/", views.posts, name="posts"),  # Blog posts page
]
