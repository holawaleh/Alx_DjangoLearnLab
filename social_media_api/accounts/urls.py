from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('posts/', views.PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', views.CommentListCreateView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/like/', views.LikePostView.as_view(), name='like-post'),
    path('users/<int:user_id>/follow/', views.follow_user, name='follow-user'),
    path('users/<int:user_id>/unfollow/', views.unfollow_user, name='unfollow-user'),
    path('users/<int:user_id>/followers/', views.user_followers, name='user-followers'),
    path('users/<int:user_id>/following/', views.user_following, name='user-following'),
]