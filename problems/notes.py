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

print('\nCLASS METHOD: create_series')
print(lord_of_the_rings)  # series (list)
# [The Fellowship of the Ring by J.R.R. Tolkien, The Two Towers by J.R.R. Tolkien, The Return of the King by J.R.R. Tolkien]

# Unpack the lord_of_the_rings list into the individual books.
fellowship_of_the_ring, two_towers, return_of_the_king = lord_of_the_rings

print(fellowship_of_the_ring)  # The Fellowship of the Ring by J.R.R. Tolkien
print(two_towers)  # The Two Towers by J.R.R. Tolkien
print(return_of_the_king)  # The Return of the King by J.R.R. Tolkien

# Call the static `Book.getTitles()` method
# to get a list of the book titles.
book_titles = Book.get_titles(
    fellowship_of_the_ring,
    two_towers,
    return_of_the_king)

print('\nSTATIC METHOD: get_titles')
print(", ".join(book_titles))
# The Fellowship of the Ring, The Two Towers, The Return of the King


# Decorators
# Python Decorators
print('\nPython Decorators')

def say_hi(name):
  print(f'Hi, {name}!')

def say_good_morning(name):
  print(f'Good morning, {name}!')

def say_something_to_curtis(say_something_func):
  return say_something_func('Curtis')

say_something_to_curtis(say_hi)            # Hi, Curtis!
say_something_to_curtis(say_good_morning)  # Good morning, Curtis!

print(say_hi)       # <function say_hi at 0x1037a41f0>
print(dir(say_hi))  # ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

print(say_hi.__closure__) # None

def say_hi_to(name):
  def say_from(author):
    print(f'Hi, {name}!')
    print(f'- Message from {author}.')
  return say_from

say_hi_ryan_from = say_hi_to('Ryan')
say_hi_ryan_from('Julia')             # Hi, Ryan! Message from Julia.
say_hi_ryan_from('Erik')              # Hi, Ryan! Message from Erik.

print(say_hi_ryan_from.__closure__)   # (<cell at 0x1093cf1f0: str object at 0x1094035f0>,)
print(say_hi_ryan_from.__closure__[0].cell_contents)  # Ryan

say_hi_andrew_from = say_hi_to('Andrew')
say_hi_chris_from = say_hi_to('Chris')
say_hi_andrew_from('Kate')       # Hi, Andrew! Message from Kate.
say_hi_chris_from('Julia')        # Hi, Chris! Message from Julia.


# What if you want your decorated function to take in arguments? You can start by explicitly setting parameters for the needed arguments...
def message_decorator(message_func):
  def message_wrapper(name, author):
    return f'{message_func(name)} ! This is a message from {author}.'
  return message_wrapper

@message_decorator
def say_hi(name):
  return f'Hi, {name}'

print(say_hi('Julia', 'Ryan'))  # Hi, Julia! This is a message from Ryan.

# ...Then you can refactor to make use of *args and **kwargs because a decorator function with explicitly set parameters isn't very reusable:
def message_decorator(message_func):
  def message_wrapper(*args):
    name, author = args  # destructures the positional arguments stored in *args
    message = message_func(name)
    return f'{message} !! This is a message from {author}.'
  return message_wrapper

@message_decorator
def say_hi(name):
  return f'Hi, {name}'

print(say_hi('Julia', 'Ryan'))  # Hi, Julia! This is a message from Ryan.

print('\nBuilt-in class decorators')
class Ring:
  def __init__(self):
    self._nickname = "Shiny ring"

  @property
  def nickname(self):
    return self._nickname

  @nickname.setter
  def nickname(self, value):
    self._nickname = value

  @nickname.deleter
  def nickname(self):
    del self._nickname
    print('Oh no! The ring is gone!')

ring = Ring()
print(ring.nickname)                  # Shiny ring
ring.nickname = "Gollum's precious"
print(ring.nickname)                  # Gollum's precious
del ring.nickname                     # Oh no! The ring is gone!
