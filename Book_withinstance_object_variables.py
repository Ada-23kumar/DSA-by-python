# Define a class Book with instance object variables bookid, title and price. Initialise
# them via __init__() method. Also define method to show book variables.
class Book:
    def __init__(self,bookid,title,price):
        self.bookid = bookid
        self.title = title
        self.price = price
    def show_book(self):
        print(f"book id = {self.bookid} book title = {self.title} book peice = {self.price}")

obj = Book(1, "adarsh", 500)
obj.show_book()
