import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# ✅ Query all books by a specific author
author = Author.objects.get(name="John Doe")
books_by_author = Book.objects.filter(author=author)
print("Books by", author.name)
for book in books_by_author:
    print("-", book.title)

# ✅ List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("\nBooks in", library.name)
for book in books_in_library:
    print("-", book.title)

# ✅ Retrieve the librarian for a library
library = Library.objects.get(name="Central Library")
librarian = library.librarian
print("\nLibrarian of", library.name, ":", librarian.name)
