def say_hi(name):
  print(f'Hi, {name}!')

def say_good_morning(name):
  print(f'Good morning, {name}!')

def say_something_to_curtis(say_something_func):
  return say_something_func('Curtis')

say_something_to_curtis(say_hi)            # Hi, Curtis!
say_something_to_curtis(say_good_morning)  # Good morning, Curtis!

# print(say_hi)       # <function say_hi at 0x1037a41f0>
# print(dir(say_hi))  # ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

from datetime import date

class Book:
    loan_duration = 14  # days - CLASS variable

    def __init__(self, title, series, author):
        self._title = title
        self._series = series
        self._author = author
        self._checked_out_on = None

    def __repr__(self):
        # without __repr__, print(fellowship_of_the_ring) returns:
        # <__main__.Book object at 0x0000028386730FD0>
        return f"{self._title} by {self._author}"
        # return 'custom string'

    def checkout(self, checked_out_on=date.today()):
        # Method to checkout a book.
        self._checked_out_on = checked_out_on

    def is_overdue(self):
        # Method to check if a book is overdue.
        overdue = False
        if self._checked_out_on is not None:
            elapsed_days = (date.today() - self._checked_out_on).days
            overdue = elapsed_days > self.loan_duration
        return overdue

    @classmethod
    def create_series(cls, series, author, *args):
        # Factory class method for creating a series of books.
        return [cls(title, series, author) for title in args]

    @staticmethod
    def get_titles(*args):
        # Static method that accepts a variable number
        # of Book instances and returns a list of their titles.
        return [book._title for book in args]


fellowship_of_the_ring = Book(
    "The Fellowship of the Ring",
    "The Lord of the Rings",
    "J.R.R. Tolkien")
grapes_of_wrath = Book(
    "The Grapes of Wrath",
    None,
    "John Steinbeck")

print(fellowship_of_the_ring)  # The Fellowship of the Ring by J.R.R. Tolkien
print(grapes_of_wrath)  # The Grapes of Wrath by John Steinbeck

fellowship_of_the_ring.checkout()   # checked out today, 0 days elapsed
print(fellowship_of_the_ring.is_overdue())  # False

# Checkout "The Fellowship of the Ring" on past date:
fellowship_of_the_ring.checkout(
    checked_out_on=date.fromisoformat("2020-04-01"))
print(fellowship_of_the_ring.is_overdue())  # True

# Call class method to create a series of books.
# @classmethod    # (reminder of class method from above)
# def create_series(cls, series, author, *args):
lord_of_the_rings = Book.create_series(
    "The Lord of the Rings",      # series
    "J.R.R. Tolkien",             # author
    "The Fellowship of the Ring", # args
    "The Two Towers",             # args
    "The Return of the King")     # args

print(lord_of_the_rings)
# [The Fellowship of the Ring by J.R.R. Tolkien, The Two Towers by J.R.R. Tolkien, The Return of the King by J.R.R. Tolkien]
