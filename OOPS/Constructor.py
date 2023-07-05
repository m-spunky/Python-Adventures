# Constructor sets the value of variables at a time of class intialliziation
class Book:
    # CONSTRUCTOR
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
    # RETURNS WHEN CONSTRUCTOR EVOKE
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"

book1 = Book('Book 1', 12, 'Author 1', 120)
book2 = Book('Book 2', 18, 'Author 2', 220)

print(book1)
print(book2)
