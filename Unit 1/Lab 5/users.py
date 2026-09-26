class user:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self._password = password
        self.borrowed_books = []

    def show_user_info(self):
        return f"{self.id} - {self.name}"
