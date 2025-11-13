from src.library import Library
from src.book import Book
from src.borrower import Borrower

def print_menu():
    """Prints the main menu options."""
    print("\n--- 📚 Library Management System Menu ---")
    print(" 1. Add New Book")
    print(" 2. Update Book Details/Quantity")
    print(" 3. Remove Book")
    print(" 4. List All Books")
    print(" ---")
    print(" 5. Add New Borrower")
    print(" 6. Update Borrower Info")
    print(" 7. Remove Borrower")
    print(" 8. List All Borrowers")
    print(" ---")
    print(" 9. Borrow Book")
    print(" 10. Return Book")
    print(" 11. Search Books")
    print(" 12. Check Overdue Books")
    print(" 0. Exit")
    print("-----------------------------------------")

# --- Helper functions for user input ---

def get_book_details():
    title = input("Enter title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    genre = input("Enter genre: ")
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity must be zero or more.")
                continue
            return Book(title, author, isbn, genre, quantity)
        except ValueError:
            print("Invalid input for quantity. Please enter a number.")

def get_borrower_details():
    name = input("Enter name: ")
    contact = input("Enter contact (phone/email): ")
    membership_id = input("Enter membership ID: ")
    return Borrower(name, contact, membership_id)

def main():
    library = Library()

    # ---pre-populating with some data---
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Classic", 5))
    library.add_book(Book("1984", "George Orwell", "9780451524935", "Dystopian", 3))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "9780061120084", "Fiction", 0))
    library.add_borrower(Borrower("Alice Smith", "alice@email.com", "M001"))
    library.add_borrower(Borrower("Bob Johnson", "555-1234", "M002"))
    print("\nWelcome to the Library Management System!")
    print("Demo data has been pre-populated.")

    while True:
        print_menu()
        choice = input("Enter your choice (0-12): ")

        try:
            if choice == '1':
                print("\n--- Add New Book ---")
                book = get_book_details()
                library.add_book(book)

            elif choice == '2':
                print("\n--- Update Book Details/Quantity ---")
                isbn = input("Enter ISBN of book to update: ")
                book = library.find_book_by_isbn(isbn)
                if book:
                    print(f"Updating: {book.title}")
                    title = input("Enter new title (or press Enter to skip): ")
                    author = input("Enter new author (or press Enter to skip): ")
                    genre = input("Enter new genre (or press Enter to skip): ")
                    library.update_book_details(isbn,
                                            title if title else None,
                                            author if author else None,
                                            genre if genre else None)

                    qty_choice = input("Do you want to update quantity? (y/n): ").lower()
                    if qty_choice == 'y':
                        try:
                            new_quantity = int(input(f"Enter new quantity (current: {book.quantity}): "))
                            library.update_book_quantity(isbn, new_quantity)
                        except ValueError:
                            print("Invalid quantity. Skipping quantity update.")
                else:
                    print(f"Error: Book with ISBN {isbn} not found.")


            elif choice == '3':
                print("\n--- Remove Book ---")
                isbn = input("Enter ISBN of book to remove: ")
                library.remove_book(isbn)

            elif choice == '4':
                library.list_all_books()

            elif choice == '5':
                print("\n--- Add New Borrower ---")
                borrower = get_borrower_details()
                library.add_borrower(borrower)

            elif choice == '6':
                print("\n--- Update Borrower Info ---")
                membership_id = input("Enter membership ID of borrower to update: ")
                if library.find_borrower_by_id(membership_id):
                    name = input("Enter new name (or press Enter to skip): ")
                    contact = input("Enter new contact (or press Enter to skip): ")
                    library.update_borrower_info(membership_id,
                                             name if name else None,
                                             contact if contact else None)
                else:
                    print(f"Error: Borrower with ID {membership_id} not found.")


            elif choice == '7':
                print("\n--- Remove Borrower ---")
                membership_id = input("Enter membership ID of borrower to remove: ")
                library.remove_borrower(membership_id)

            elif choice == '8':
                library.list_all_borrowers()

            elif choice == '9':
                print("\n--- Borrow Book ---")
                membership_id = input("Enter your membership ID: ")
                isbn = input("Enter book ISBN to borrow: ")
                library.borrow_book(membership_id, isbn)

            elif choice == '10':
                print("\n--- Return Book ---")
                membership_id = input("Enter your membership ID: ")
                isbn = input("Enter book ISBN to return: ")
                library.return_book(membership_id, isbn)

            elif choice == '11':
                print("\n--- Search Books ---")
                title = input("Enter title (or press Enter to skip): ")
                author = input("Enter author (or press Enter to skip): ")
                genre = input("Enter genre (or press Enter to skip): ")

                results = library.search_book(title if title else None,
                                            author if author else None,
                                            genre if genre else None)
                if results:
                    print(f"\nFound {len(results)} book(s):")
                    for book in results:
                        print(book)
                else:
                    print("No books found matching the criteria.")

            elif choice == '12':
                library.list_overdue_books()

            elif choice == '0':
                print("\nExiting the system. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 0 and 12.")

        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
