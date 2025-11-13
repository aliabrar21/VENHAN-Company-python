class Borrower:
    """
    Represents a library borrower.

    Attributes:
        name (str): The borrower's name.
        contact (str): The borrower's contact details (phone/email).
        membership_id (str): The borrower's unique membership ID.
        borrowed_books (list): A list of tuples, where each tuple contains
                               (book_object, due_date).
    """
    def __init__(self, name, contact, membership_id):
        self.name = name
        self.contact = contact
        self.membership_id = membership_id
        self.borrowed_books = []  # List to track (book_object, due_date)

    def update_contact(self, new_contact):
        self.contact = new_contact
        print(f"Contact updated for {self.name}.")

    def update_name(self, new_name):
        self.name = new_name
        print(f"Name updated for {self.membership_id}.")

    def __str__(self):
        return (f"Name: {self.name}, ID: {self.membership_id}, "
                f"Contact: {self.contact}, Books Borrowed: {len(self.borrowed_books)}")
