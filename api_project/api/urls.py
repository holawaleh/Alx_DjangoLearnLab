# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # path('books/', BookList.as_view(), name='book-list'),  # URL for the BookList view
     path('', include(router.urls)),  # Includes all routes registered with the router

]