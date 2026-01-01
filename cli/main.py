from library_manager.inventory import LibraryInventory

def menu():
    print("\n--- Library Inventory Manager ---")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All Books")
    print("5. Search Book")
    print("6. Exit")

def main():
    inventory = LibraryInventory()

    while True:
        menu()
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                inventory.add_book(title, author, isbn)

            elif choice == "2":
                isbn = input("ISBN to issue: ")
                book = inventory.search_by_isbn(isbn)
                if book and book.issue():
                    print("Book issued.")
                    inventory.save_data()
                else:
                    print("Book not available.")

            elif choice == "3":
                isbn = input("ISBN to return: ")
                book = inventory.search_by_isbn(isbn)
                if book:
                    book.return_book()
                    inventory.save_data()
                    print("Book returned.")

            elif choice == "4":
                inventory.display_all()

            elif choice == "5":
                title = input("Enter title keyword: ")
                results = inventory.search_by_title(title)
                for b in results:
                    print(b)

            elif choice == "6":
                print("Exiting...")
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
