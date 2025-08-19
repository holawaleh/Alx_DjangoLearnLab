# bookshelf/urls.py
from django.urls import path
from . import views

app_name = 'bookshelf'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('libraries/', views.library_list, name='library_list'),
    path('books/author/<str:author_name>/', views.books_by_author, name='books_by_author'),
]