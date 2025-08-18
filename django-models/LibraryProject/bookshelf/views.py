# bookshelf/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Bookshelf!")

def book_list(request):
    return HttpResponse("List of all books.")

def book_detail(request, book_id):
    return HttpResponse(f"Detail view for book ID: {book_id}")

def library_list(request):
    return HttpResponse("List of libraries.")

def books_by_author(request, author_name):
    return HttpResponse(f"Books by author: {author_name}")