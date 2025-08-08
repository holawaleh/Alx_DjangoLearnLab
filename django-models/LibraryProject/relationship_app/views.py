from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import DetailView
from django.contrib import messages

from .models import Book, Library

# --- Function-Based View ---
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# --- Class-Based View ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# --- Auth Views ---
def user_login(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('list_books')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('list_books')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'relationship_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, 'relationship_app/logout.html')

def register(request):
    if request.user.is_authenticated:
        messages.info(request, "You already have an account.")
        return redirect('list_books')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('list_books')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, 'relationship_app/register.html', {'form': form})
