from django.shortcuts import render, get_object_or_404
from .models import Author, Book, Library, Librarian

# Home view
def home(request):
    return render(request, 'relationship_app/home.html')

# List all books
def book_list(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

# Book detail
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'relationship_app/book_detail.html', {'book': book})

# List all libraries
def library_list(request):
    libraries = Library.objects.select_related('librarian').all()
    return render(request, 'relationship_app/library_list.html', {'libraries': libraries})

# Filter books by author name
def books_by_author(request, author_name):
    books = Book.objects.filter(author__name__icontains=author_name)
    return render(request, 'relationship_app/book_list.html', {'books': books})
