from datetime import datetime, timedelta
from .book import Book
from .borrower import Borrower

class Library:
    """
    Manages the library's collection of books, borrowers, and transactions.

    Attributes:
        books (list): A list of Book objects.
        borrowers (list): A list of Borrower objects.
    """
    def __init__(self):
        self.books = []
        self.borrowers = []

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_borrower_by_id(self, membership_id):
        for borrower in self.borrowers:
            if borrower.membership_id == membership_id:
                return borrower
        return None

    def add_book(self, book):
        if self.find_book_by_isbn(book.isbn):
            print(f"Error: Book with ISBN {book.isbn} already exists.")
            return False
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")
        return True

    def update_book_details(self, isbn, title=None, author=None, genre=None):
        book = self.find_book_by_isbn(isbn)
        if book:
            book.update_details(title=title, author=author, genre=genre)
            return True
        print(f"Error: Book with ISBN {isbn} not found.")
        return False

    def update_book_quantity(self, isbn, new_quantity):
        book = self.find_book_by_isbn(isbn)
        if book:
            book.update_quantity(new_quantity)
            print(f"Book {isbn} quantity updated to {new_quantity}.")
            return True
        print(f"Error: Book with ISBN {isbn} not found.")
        return False

    def remove_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book:
            # Check if book is currently borrowed
            for borrower in self.borrowers:
                for borrowed_book, _ in borrower.borrowed_books:
                    if borrowed_book.isbn == isbn:
                        print(f"Error: Cannot remove '{book.title}'. It is currently borrowed by {borrower.name}.")
                        return False

            self.books.remove(book)
            print(f"Book '{book.title}' removed successfully.")
            return True
        print(f"Error: Book with ISBN {isbn} not found.")
        return False



    def add_borrower(self, borrower):
        if self.find_borrower_by_id(borrower.membership_id):
            print(f"Error: Borrower with ID {borrower.membership_id} already exists.")
            return False
        self.borrowers.append(borrower)
        print(f"Borrower '{borrower.name}' added successfully.")
        return True

    def update_borrower_info(self, membership_id, name=None, contact=None):
        borrower = self.find_borrower_by_id(membership_id)
        if borrower:
            if name:
                borrower.update_name(name)
            if contact:
                borrower.update_contact(contact)
            print(f"Borrower {membership_id} info updated.")
            return True
        print(f"Error: Borrower with ID {membership_id} not found.")
        return False

    def remove_borrower(self, membership_id):
        borrower = self.find_borrower_by_id(membership_id)
        if borrower:
            if borrower.borrowed_books:
                print(f"Error: Cannot remove {borrower.name}. They have outstanding borrowed books.")
                return False

            self.borrowers.remove(borrower)
            print(f"Borrower '{borrower.name}' removed successfully.")
            return True
        print(f"Error: Borrower with ID {membership_id} not found.")
        return False

    def borrow_book(self, membership_id, isbn):
        borrower = self.find_borrower_by_id(membership_id)
        book = self.find_book_by_isbn(isbn)

        if not borrower:
            print(f"Error: Borrower {membership_id} not found.")
            return False
        if not book:
            print(f"Error: Book {isbn} not found.")
            return False

        if not book.is_available():
            print(f"Error: Book '{book.title}' is out of stock.")
            return False

        for b, _ in borrower.borrowed_books:
            if b.isbn == isbn:
                print(f"Error: {borrower.name} has already borrowed a copy of '{book.title}'.")
                return False

        book.update_quantity(book.quantity - 1)
        due_date = datetime.now() + timedelta(days=14)
        borrower.borrowed_books.append((book, due_date))
        print(f"Book '{book.title}' borrowed by {borrower.name}. Due: {due_date.strftime('%Y-%m-%d')}")
        return True

    def return_book(self, membership_id, isbn):
        borrower = self.find_borrower_by_id(membership_id)
        if not borrower:
            print(f"Error: Borrower {membership_id} not found.")
            return False

        book_to_return_tuple = None
        for item in borrower.borrowed_books:
            book_obj, due_date = item
            if book_obj.isbn == isbn:
                book_to_return_tuple = item
                break

        if not book_to_return_tuple:
            print(f"Error: Borrower {membership_id} has not borrowed book {isbn}.")
            return False

        book_obj, due_date = book_to_return_tuple
        borrower.borrowed_books.remove(book_to_return_tuple)

        main_book = self.find_book_by_isbn(isbn)
        if main_book:
            main_book.update_quantity(main_book.quantity + 1)

        print(f"Book '{book_obj.title}' returned by {borrower.name}.")

        if datetime.now() > due_date:
            overdue_days = (datetime.now() - due_date).days
            print(f"**ALERT: This book is {overdue_days} day(s) overdue!**")

        return True

    def search_book(self, title=None, author=None, genre=None):
        results = []
        for book in self.books:
            match = True
            if title and title.lower() not in book.title.lower():
                match = False
            if author and author.lower() not in book.author.lower():
                match = False
            if genre and genre.lower() not in book.genre.lower():
                match = False

            if match:
                results.append(book)
        return results

    def list_all_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\n--- All Books in Library ---")
        for book in self.books:
            print(book)

    def list_all_borrowers(self):
        if not self.borrowers:
            print("No borrowers in the system.")
            return
        print("\n--- All Registered Borrowers ---")
        for borrower in self.borrowers:
            print(borrower)

    def list_overdue_books(self):
        overdue_found = False
        today = datetime.now()
        print("\n--- Overdue Books Report ---")
        for borrower in self.borrowers:
            for book, due_date in borrower.borrowed_books:
                if today > due_date:
                    overdue_days = (today - due_date).days
                    print(f"  - Borrower: {borrower.name} (ID: {borrower.membership_id})")
                    print(f"    Book: '{book.title}' (ISBN: {book.isbn})")
                    print(f"    Due Date: {due_date.strftime('%Y-%m-%d')} ({overdue_days} days overdue)")
                    overdue_found = True

        if not overdue_found:
            print("No overdue books.")
