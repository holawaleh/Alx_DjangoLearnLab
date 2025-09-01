from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    UserProfileView,
    PostListCreateView,
    PostDetailView,
    CommentListCreateView,
    LikePostView,
    follow_user,
    unfollow_user,
    user_followers,
    user_following,
)

urlpatterns = [
    # 🔹 Authentication
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),

    # 🔹 Posts & Engagement
    path("posts/", PostListCreateView.as_view(), name="post-list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:post_id>/comments/", CommentListCreateView.as_view(), name="comment-list"),
    path("posts/<int:post_id>/like/", LikePostView.as_view(), name="like-post"),

    # 🔹 Follow System
    path("users/<int:user_id>/follow/", follow_user, name="follow-user"),
    path("users/<int:user_id>/unfollow/", unfollow_user, name="unfollow-user"),
    path("users/<int:user_id>/followers/", user_followers, name="user-followers"),
    path("users/<int:user_id>/following/", user_following, name="user-following"),
]
