class Book:
    def __init__(self, title, author, is_borrowed):
        self.title=title
        self.author=author
        self.is_borrowed=False

    
    
    def borrow(self):
        self.is_borrowed=True
        print(self.title, "(", self.author, ") has been borrowed")

    def return_book(self):
        self.is_borrowed=False
        print(self.title, "(", self.author, ") has been returned")

TGG=Book("The Great Gatsby", "F. Scott Fitzgerald", False)
TGG.borrow()
TGG.return_book()
SH=Book("The Adventures of Sherlock Holmes", "Sir Arthur Conan Doyle", False)
SH.borrow()
SH.return_book()
AF=Book("Animal Farm", "George Orwell", False)
AF.borrow()
AF.return_book()
AoGG=Book("Anne of Green Gables", "L.M. Montgomery", False)
AoGG.borrow()
AoGG.return_book()


