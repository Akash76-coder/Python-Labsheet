# CRUD operations on books

books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        books.append(name)
        print("Book added successfully.")

    elif choice == "2":
        print("Books:", books)

    elif choice == "3":
        old_name = input("Enter old book name: ")
        if old_name in books:
            new_name = input("Enter new book name: ")
            index = books.index(old_name)
            books[index] = new_name
            print("Book updated successfully.")
        else:
            print("Book not found.")

    elif choice == "4":
        name = input("Enter book name: ")
        if name in books:
            books.remove(name)
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")