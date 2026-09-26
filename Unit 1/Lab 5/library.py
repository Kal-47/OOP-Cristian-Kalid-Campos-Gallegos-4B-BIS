class library:
    def __init__(self):
        self.users = []
        self.books = []

    def add_users(self, user):
        self.users.append(user)

    def add_books(self, book):
        self.books.append(book)

    def show_books_list(self):
        for book in self.books:
            print(book.show_book_info())

    def find_book(self, id_book):
        for book in self.books:
            if book.id_book == id_book:
                return book
        return None

    def find_user(self, id_user):
        for user in self.users:
            if user.id == id_user:
                return user
        return None

    def borrow_book(self, id_book, id_user):
        target_book = self.find_book(id_book)
        target_user = self.find_user(id_user)

        if target_book is None:
            print(f"Book {id_book} not found.")
            return
        if target_user is None:
            print(f"User {id_user} not found.")
            return
        if target_book.borrowed:
            print(f"'{target_book.title}' is already borrowed and cannot be borrowed again.")
            return

        target_book.borrowed = True
        target_book.borrowed_by = target_user.id
        target_user.borrowed_books.append(target_book.id_book)
        print(f"'{target_book.title}' was borrowed by {target_user.name}.")

    def return_book(self, id_book):
        target_book = self.find_book(id_book)

        if target_book is None:
            print(f"Book {id_book} not found.")
            return
        if not target_book.borrowed:
            print(f"'{target_book.title}' was not borrowed, so it cannot be returned.")
            return

        target_user = self.find_user(target_book.borrowed_by)
        if target_user and target_book.id_book in target_user.borrowed_books:
            target_user.borrowed_books.remove(target_book.id_book)

        target_book.borrowed = False
        target_book.borrowed_by = None
        print(f"'{target_book.title}' was returned.")
