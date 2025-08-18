from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required  # Optional: for protected pages
from django.views.generic import DetailView
from .models import Book, Library

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log them in automatically
            return redirect('list_books')  # Redirect to book list
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})


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