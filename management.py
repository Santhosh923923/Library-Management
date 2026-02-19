import mysql.connector

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",        # change if needed
    password="Digidara1000",  # change to your mysql password
    database="librarydb"
)

cursor = conn.cursor()


class Book:
    def __init__(self, bookid, booktitle, authorname, status="available"):
        self.bookid = bookid
        self.booktitle = booktitle
        self.authorname = authorname
        self.status = status

    def __str__(self):
        return f"id={self.bookid} title={self.booktitle} author={self.authorname} status={self.status}"


class Library:

    def addbook(self):
        bookid = int(input("Enter book id: "))
        booktitle = input("Enter book title: ")
        authorname = input("Enter author name: ")

        sql = "INSERT INTO books (bookid, booktitle, authorname, status) VALUES (%s, %s, %s, %s)"
        values = (bookid, booktitle, authorname, "available")

        try:
            cursor.execute(sql, values)
            conn.commit()
            print("Book added successfully")
        except mysql.connector.Error as err:
            print("Error:", err)

    def showbook(self):
        cursor.execute("SELECT * FROM books")
        records = cursor.fetchall()

        if not records:
            print("No books found")
            return

        for row in records:
            print(f"id={row[0]} title={row[1]} author={row[2]} status={row[3]}")
        print()

    def borrowbook(self):
        bookid = int(input("Enter book id to borrow: "))

        cursor.execute("SELECT status FROM books WHERE bookid=%s", (bookid,))
        result = cursor.fetchone()

        if not result:
            print("Book not found")
            return

        if result[0] == "available":
            cursor.execute("UPDATE books SET status='borrowed' WHERE bookid=%s", (bookid,))
            conn.commit()
            print("Book borrowed successfully")
        else:
            print("Book already borrowed")

    def returnbook(self):
        bookid = int(input("Enter book id to return: "))

        cursor.execute("SELECT status FROM books WHERE bookid=%s", (bookid,))
        result = cursor.fetchone()

        if not result:
            print("Book not found")
            return

        if result[0] == "borrowed":
            cursor.execute("UPDATE books SET status='available' WHERE bookid=%s", (bookid,))
            conn.commit()
            print("Book returned successfully")
        else:
            print("Book was not borrowed")

    def menu(self):
        while True:
            print("\nLibrary Menu")
            print("1. Add Book")
            print("2. Show Books")
            print("3. Borrow Book")
            print("4. Return Book")
            print("5. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.addbook()
            elif choice == "2":
                self.showbook()
            elif choice == "3":
                self.borrowbook()
            elif choice == "4":
                self.returnbook()
            elif choice == "5":
                print("Exiting Library System")
                break
            else:
                print("Invalid choice")


lib = Library()
lib.menu()

cursor.close()
conn.close()
