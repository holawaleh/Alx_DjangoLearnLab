from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import User
from posts.models import Post, Comment, Like
from .serializers import (
    TokenUserRegistrationSerializer,
    TokenUserLoginSerializer,
    UserSerializer,
    PostSerializer,
    CommentSerializer,
    LikeSerializer,
)


# --- Auth ---
class RegisterView(generics.CreateAPIView):
    serializer_class = TokenUserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = TokenUserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


# --- Profile ---
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# --- Posts ---
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# --- Comments ---
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs["post_id"])

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        serializer.save(author=self.request.user, post=post)


# --- Likes ---
class LikePostView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            like.delete()
            return Response({"message": "Unliked"})
        return Response({"message": "Liked"})


# --- Follow System ---
@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    request.user.following.add(target_user)
    return Response({"message": f"You are now following {target_user.username}"})


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(User, id=user_id)
    request.user.following.remove(target_user)
    return Response({"message": f"You unfollowed {target_user.username}"})


@api_view(["GET"])
def user_followers(request, user_id):
    user = get_object_or_404(User, id=user_id)
    serializer = UserSerializer(user.followers.all(), many=True)
    return Response(serializer.data)


@api_view(["GET"])
def user_following(request, user_id):
    user = get_object_or_404(User, id=user_id)
    serializer = UserSerializer(user.following.all(), many=True)
    return Response(serializer.data)
