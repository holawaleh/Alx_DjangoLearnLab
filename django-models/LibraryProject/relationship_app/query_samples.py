import os
import django

# Setup Django environment so the script works standalone
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
# ✅ List all books in a specific library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print("-", book.title)

# -------------------------------
# ✅ Get the librarian for a library
librarian = library.librarian  # Uses related_name from the OneToOneField
print(f"\nLibrarian for {library.name}: {librarian.name}")
