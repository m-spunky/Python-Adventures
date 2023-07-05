# Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only on usage of it. 
# from Objects import Chair
from Encapsulation import Book

class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

print(academic1)