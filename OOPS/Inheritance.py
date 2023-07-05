# Inheritance is the procedure in which one class inherits the attributes and methods of another class.
# class Ferrari(Car):
class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        # TAKING VALUE FROM PARENT CLASS
        super().__init__(title, quantity, author, price)
        self.pages = pages

novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)

print(novel1)