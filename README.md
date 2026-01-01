# 📚 Library Inventory Manager

## Introduction
This project is a simple **Library Inventory Manager** made using Python.  
It is a **command-line program** that helps manage books in a library.

Using this program, a user can:
- Add new books
- Issue a book
- Return a book
- Search for books
- View all books in the library

This project is created for learning **Object-Oriented Programming (OOP)** and basic **file handling** in Python.

---

## What This Project Does
The program keeps a record of books in a library.  
Each book has:
- Title
- Author
- ISBN number
- Status (available or issued)

All book data is saved in a file so that the information is **not lost** when the program is closed.

---

## Project Structure 
library-inventory-manager-Krishyangi/
├── library_manager/
│ ├── book.py → contains the Book class
│ ├── inventory.py → manages all books
│
├── cli/
│ └── main.py → runs the menu-based program
│
├── data/
│ └── books.json → stores book data
│
├── README.md
├── requirements.txt
└── .gitignore


- `book.py` handles **single book details**
- `inventory.py` handles **all books together**
- `main.py` shows the **menu and user options**
- `books.json` stores the data permanently

---

## How the Program Works
1. The program starts by showing a menu
2. The user selects an option by entering a number
3. Based on the choice, the program performs the action
4. Book data is saved automatically in a JSON file

---

## Object-Oriented Programming Used
This project uses OOP concepts:
- **Class** – Book and LibraryInventory
- **Objects** – Each book is an object
- **Methods** – Used to issue, return, and search books
- **Encapsulation** – Data and functions are grouped together

---

## File Handling
- Book data is saved in `books.json`
- JSON format is used because it is easy to read and write
- The program safely handles missing or empty files

---

## Author
Name: Krishyangi Dixit
Course: Programming for Problem Solving using Python  
---

