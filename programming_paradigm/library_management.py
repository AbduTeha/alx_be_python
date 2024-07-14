class Book:
    """
    Represents a book with title, author, and availability status.
    """

    def __init__(self, title, author):
        """
        Initializes a Book object with title, author, and availability (not checked out).

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute for availability

    def check_out(self):
        """
        Marks the book as checked out (unavailable).
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as returned (available).
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Returns True if the book is available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the book (title by author).
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Represents a library with a collection of books and methods for managing them.
    """

    def __init__(self):
        """
        Initializes a Library object with an empty list of books.
        """
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Attempts to check out a book by title, marking it as unavailable if found.

        Args:
            title (str): The title of the book to check out.

        Returns:
            bool: True if the book is checked out successfully, False otherwise (not found).
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """
        Attempts to return a book by title, marking it as available if found.

        Args:
            title (str): The title of the book to return.

        Returns:
            bool: True if the book is returned successfully, False otherwise (not found).
        """
        for book in self._books:
            if book.title == title:
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """
        Prints a list of titles of all available books in the library.
        """
        print("Available books:")
        for book in self._books:
            if book.is_available():
                print(book)
