# Library Management System

books = ["Python", "Java", "C++"]
details = ("Library", "2026")

def display():
    for book in books:
        print(book)

while True:
    print("\n1. Display Books")
    print("2. Borrow Book")
    print("3. Save File")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display()

    elif choice == "2":
        book = input("Enter book name: ")
        if book in books:
            books.remove(book)
            print("Book borrowed!")
        else:
            print("Book not available!")

    elif choice == "3":
        with open("books.txt", "w") as f:
            for book in books:
                f.write(book + "\n")
        print("File saved!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
