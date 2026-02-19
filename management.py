class Book:
    def __init__(self, bookid, booktitle, authorname):
        self.bookid = bookid
        
        self.booktitle = booktitle
        self.authorname = authorname
        self.status = "available"
        

    def __str__(self):
        return f"id={self.bookid} title={self.booktitle} author={self.authorname} status={self.status}"

    
    
class Library:
    def __init__(self):
        self.books=[]
        
    def addbook(self):
        bookid=int(input("enter the book id"))
        booktitle=input("enter the book title")
        authorname=input("enter the authorname")
        new=Book(bookid,booktitle,authorname)
        self.books.append(new)
        print(f"{booktitle} book added successfully")
        
    def showbook(self):
        if not self.books:
            print("no book exists")
            return
        for book in self.books:
            print(book)
        print()
        
    def borrowbook(self):
        if not self.books:
            print("no book exists")
            return
        try:
            bookid = int(input("enter the book id to borrow: "))
        except ValueError:
            print("invalid book id")
            return
        for book in self.books:
            if book.bookid == bookid:
                if book.status == "available":
                    book.status = "borrowed"
                    print("book borrowed successfully")
                    return
                else:
                    print("the book is already borrowed")
                    return
        print("book not found")
    def returnbook(self):
        if not self.books:
            print("no book exists")
            return
        try:
            bookid = int(input("enter the book id to return: "))
        except ValueError:
            print("invalid book id")
            return
        for book in self.books:
            if book.bookid == bookid:
                if book.status == "borrowed":
                    book.status = "available"
                    print("the book is now available")
                    return
                else:
                    print("that book was not borrowed")
                    return
        print("book not found")

    def menu(self):
       while True:
        print("library menu")
        print("1.add books")
        print("2.show books")
        print("3.borrow book")
        print("4.return book")
        print("5.exit") 

        choice=input("choose an option")
        if choice=="1":
            self.addbook()
        elif choice=="2":
            self.showbook()
        elif choice=="3":
            self.borrowbook()
        elif choice=="4":
            self.returnbook()
        elif choice=="5":
             print("library manegement systyems ")
             break
        else:
            print("invalid")

lib=Library() 
lib.menu()