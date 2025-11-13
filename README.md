# 📚 Library Management System (Python OOP)

A clean, console-based **Library Management System** built using **Python** and **Object-Oriented Programming (OOP)** principles.
Designed for the **VENHAN Backend Assignment**, focusing on structured design, encapsulation, and efficient in-memory data handling — no external database required.

---

## 🚀 Features

### 🧩 Book Management
- Add, update, and remove books
- Track book details — *title, author, genre, and quantity*

### 👥 Borrower Management
- Register new borrowers
- Update borrower information
- Remove borrowers from the system

### 🔄 Transaction Handling
- Borrow books (checks stock & sets a **14-day due date**)
- Return books (updates stock & checks **overdue status**)

### 🔍 Search & Reporting
- Search books by **title**, **author**, or **genre**
- Display available book quantities
- View all books and borrowers
- Generate **overdue book reports**

---

## 🗂️ Project Structure

```
library-management-python/
├── src/
│   ├── __init__.py
│   ├── book.py          # Defines the Book class
│   ├── borrower.py      # Defines the Borrower class
│   └── library.py       # Core Library logic (manages all operations)
├── main.py              # Entry point with console-based menu
├── README.md            # Project documentation
└── .gitignore           # Git ignore configuration
```

---

## 🏃 How to Run

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd library-management-python
```

### 2️⃣ (Optional) Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Run the Application
```bash
python3 main.py
```

### 4️⃣ Follow the On-Screen Menu
Manage books, borrowers, and transactions directly through the console.

---

## 💡 OOP Concepts Demonstrated

| Concept | Implementation |
|----------|----------------|
| **Classes & Objects** | `Book`, `Borrower`, and `Library` represent real-world entities. |
| **Encapsulation** | Each class contains its own data and logic. The `Library` class controls access to the main data structures. |
| **Modularity** | Code is divided into separate files (`book.py`, `borrower.py`, etc.) for clarity and reuse. |
| **Abstraction** | Users interact through simple commands; internal logic remains hidden. |

---


## 🧠 Summary

This project demonstrates:
- Clean OOP-based architecture
- Full in-memory management (no database)
- Simple yet effective CLI for practical library operations
- Codebase ready for future scalability and database integration

---

**Author:** Subbareddy K
**Language:** Python 3.13.9
