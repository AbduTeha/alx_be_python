class Book:
  """
  Represents a book with title, author, and publication year.
  """

  def __init__(self, title, author, year):
    """
    Initializes a Book instance.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
    """
    self.title = title
    self.author = author
    self.year = year

  def __del__(self):
    """
    Prints a message when a Book instance is deleted.
    """
    print(f"Deleting {self.title}")

  def __str__(self):
    """
    Returns a human-readable string representation of the book.

    Returns:
        str: A string in the format "(title) by (author), published in (year)".
    """
    return f"{self.title} by {self.author}, published in {self.year}"

  def __repr__(self):
    """
    Returns a string that can be used to recreate the Book instance.

    Returns:
        str: A string in the format "Book('{self.title}', '{self.author}', {self.year})".
    """
    return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage (can be placed in the same file or a separate script)
if __name__ == "__main__":
  my_book = Book("1984", "George Orwell", 1949)

  print(my_book)  # Expected to use __str__
  print(repr(my_book))  # Expected to use __repr__

  # Deleting a book instance to trigger __del__
  del my_book
