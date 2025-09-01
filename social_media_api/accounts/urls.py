from django.urls import path, include

from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('posts/', views.PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', views.CommentListCreateView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/like/', views.LikePostView.as_view(), name='like-post'),
]