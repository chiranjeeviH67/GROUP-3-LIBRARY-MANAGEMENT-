library = {}

def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    library[book_id] = {
        "title": title,
        "author": author,
        "available": True
    }
    print("Book added successfully!")

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    if book_id in library:
        if library[book_id]["available"]:
            library[book_id]["available"] = False
            print("Book issued successfully!")
        else:
            print("Book is already issued!")
    else:
        print("Book not found!")

def return_book():
    book_id = input("Enter Book ID to return: ")
    if book_id in library:
        library[book_id]["available"] = True
        print("Book returned successfully!")
    else:
        print("Book not found!")

def display_books():
    if not library:
        print("No books available.")
    else:
        for book_id, details in library.items():
            status = "Available" if details["available"] else "Issued"
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Status: {status}")

while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")
