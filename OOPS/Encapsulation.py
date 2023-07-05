# Encapsulation in Python is the process of wrapping up variables and methods into a single entity. In programming, a class is an example that wraps all the variables and methods defined inside it.
class Book:
    def __init__(self, title, quantity, author, price):
        
        # PUBLIC VARIABLES
        self.title = title
        self.quantity = quantity
        self.author = author

        # PRIVATE VARIABLES
        self.__price = price
        self.__discount = 0

    # FUNCTION FOR ACCESING PRIVATE VARIABLES
    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

single_book = Book('Two States', 1, 'Chetan Bhagat', 200)

bulk_books = Book('Two States', 25, 'Chetan Bhagat', 200)
bulk_books.set_discount(0.20)

print(single_book.get_price())
print(bulk_books.get_price())
