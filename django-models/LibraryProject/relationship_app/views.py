# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view: List all books
def list_books(request):
    """Display a list of all books with titles and authors"""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view: Display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'