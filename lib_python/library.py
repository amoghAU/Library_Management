books = []          # [book_id, title, author, available]
issued = []         # [book_id, student]

def add_book():
    id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    copies = int(input("Copies: "))
    books.append([id, title, author, copies])
    print("Book added!\n")

def view_books():
    if not books:
        print("No books\n")
        return
    for b in books:
        print(b[0], "|", b[1], "|", b[2], "| Available:", b[3])
    print()

 def search_book():
    search = input("Enter Book ID or Title to search: ").lower()
    found = False

    for b in books:
        if search == b[0].lower() or search in b[1].lower():
            print(b[0], "|", b[1], "|", b[2], "| Available:", b[3])
            found = True

    if not found:
        print("No matching book found\n")
    else:
        print()

def issue_book():
    id = input("Book ID: ")
    name = input("Student Name: ")

    for b in books:
        if b[0] == id:
            if b[3] > 0:
                b[3] -= 1
                issued.append([id, name])
                print("Issued!\n")
                return
            else:
                print("Not available\n")
                return
    print("Book not found\n")

def view_issued():
    if not issued:
        print("No issued books\n")
        return
    for i in issued:
        print("Book ID:", i[0], "| Student:", i[1])
    print()

def return_book():
    id = input("Book ID: ")

    for i in issued:
        if i[0] == id:
            issued.remove(i)
            for b in books:
                if b[0] == id:
                    b[3] += 1
            print("Returned!\n")
            return
    print("Not found in issued list\n")

def delete_book():
    id = input("Book ID to delete: ")
    for b in books:
        if b[0] == id:
            books.remove(b)
            print("Book deleted!\n")
            return
    print("Book not found\n")

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")   # NEW OPTION
    print("4. Issue Book")
    print("5. Return Book")
    print("6. View Issued Books")
    print("7. Delete Book")
    print("8. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_book()
    elif ch == "2":
        view_books()
    elif ch == "3":
        search_book()   # CALL FUNCTION
    elif ch == "4":
        issue_book()
    elif ch == "5":
        return_book()
    elif ch == "6":
        view_issued()
    elif ch == "7":
        delete_book()
    elif ch == "8":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")