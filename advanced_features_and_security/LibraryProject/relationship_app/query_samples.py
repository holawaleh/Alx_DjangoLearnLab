"""
Sample queries for relationship_app models.
Run this inside Django shell: python manage.py shell
"""

from relationship_app.models import Author, Book, Library, Librarian


def query_all_books_by_author(author_name):
    """Query: All books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()  # Uses related_name='books'
        print(f"\nBooks by {author_name}:")
        for book in books:
            print(f" - {book.title}")
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found.")


def list_all_books_in_library(library_name):
    """Query: All books in a specific library"""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books:
            print(f" - {book.title}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")


def retrieve_librarian_for_library(library_name):
    """Query: Librarian for a specific library"""
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # OneToOne reverse lookup
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")


# Optional: Add this block to prevent auto-execution
if __name__ == "__main__":
    print("This script is meant to be run inside Django shell.")