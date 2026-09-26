from books import book
from users import user
from library import library

# Instances
book1 = book("001", "OOP Fundamentals", "Jhon L", "BBC")
book2 = book("002", "Python for dummies", "Stef Maruzh", "For dummies")

user1 = user("001", "Cristian Campos", "1234")

my_library = library()
my_library.add_books(book1)
my_library.add_books(book2)
my_library.add_users(user1)

print("Initial catalog:")
my_library.show_books_list()

print("\nBorrowing book 001:")
my_library.borrow_book("001", "001")

print("\nTrying to borrow book 001 again (should be blocked):")
my_library.borrow_book("001", "001")

print("\nCatalog after borrowing:")
my_library.show_books_list()

print("\nReturning book 001:")
my_library.return_book("001")

print("\nCatalog after returning:")
my_library.show_books_list()

# Requirements
# 1. The system must allow registering books.
# 2. The system must allow registering users.
# 3. The system must allow a book to be borrowed by a user.
# 4. A book that has been borrowed cannot be borrowed again.
# 5. The system must allow a book to be returned.
