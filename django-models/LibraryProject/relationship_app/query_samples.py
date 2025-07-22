import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# -------------------------------
# ✅ Query all books by a specific author
author_name = "John Doe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

print(f"Books by {author.name}:")
for book in books_by_author:
    print("-", book.title)

# -------------------------------
# ✅ List all books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print("-", book.title)

# -------------------------------
# ✅ Get the librarian — method A (related_name)
librarian_via_related = library.librarian
print(f"\nLibrarian via related_name: {librarian_via_related.name}")

# ✅ Get the librarian — method B (objects.get)
librarian_via_query = Librarian.objects.get(library=library)
print(f"Librarian via .objects.get: {librarian_via_query.name}")
