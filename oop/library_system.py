class Book:
  """
  Represents a base book class with title and author.
  """
  def __init__(self, title, author):
    self.title = title
    self.author = author

class EBook(Book):
  """
  Represents an ebook with additional file size attribute.
  """
  def __init__(self, title, author, file_size):
    super().__init__(title, author)  # Call base class constructor
    self.file_size = file_size

class PrintBook(Book):
  """
  Represents a print book with additional page count attribute.
  """
  def __init__(self, title, author, page_count):
    super().__init__(title, author)  # Call base class constructor
    self.page_count = page_count

class Library:
  """
  Represents a library that manages a collection of books.
  """
  def __init__(self):
    self.books = []

  def add_book(self, book):
    """
    Adds a book instance (Book, EBook, or PrintBook) to the library.
    """
    self.books.append(book)

  def list_books(self):
    """
    Prints details of each book in the library.
    """
    for book in self.books:
      # Leverage polymorphism to handle different book types
      print(f"{book.title} by {book.author} ({book.__class__.__name__})")
      # Optionally, use conditional checks for specific book types if needed
      # if isinstance(book, EBook):
      #   print(f"  File size: {book.file_size} MB")
      # elif isinstance(book, PrintBook):
      #   print(f"  Page count: {book.page_count}")
