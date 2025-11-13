class Book:
    """
    Represents a single book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The unique ISBN of the book.
        genre (str): The genre of the book.
        quantity (int): The number of available copies.
    """
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Error: Quantity cannot be negative.")

    def update_details(self, title=None, author=None, genre=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre
        print(f"Book details for ISBN {self.isbn} updated.")

    def is_available(self):
        return self.quantity > 0

    def __str__(self):
        status = "Available" if self.is_available() else "Out of Stock"
        return (f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, "
                f"Genre: {self.genre}, Quantity: {self.quantity} ({status})")
