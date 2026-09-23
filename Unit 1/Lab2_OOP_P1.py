class User:
    def __init__(self, username, password, mail):
        self.username = username
        self.password = password
        self.mail = mail
        self.posts = []

    def login(self):
        print(f"{self.username} is logged in")

    def create_post(self, content):
        post = Post(content, author=self)
        self.posts.append(post)
        print(f"{self.username} created a post: {content}")
        return post


class Post:
    def __init__(self, text, author, filetype="text", n_saves=0):
        self.text = text
        self.author = author       # composición: el Post "tiene" un User (quien lo creó)
        self.filetype = filetype
        self.__n_saves = n_saves
        self.comments = []         # el Post "tiene" varios Comments

    def add_comment(self, comment):
        self.comments.append(comment)


class Comment:
    def __init__(self, comm_val, author, likes=0, dislikes=0, n_saves=0):
        self.comm_val = comm_val
        self.author = author       # el OTRO usuario que comentó
        self.likes = likes
        self.dislikes = dislikes
        self.__n_saves = n_saves


class Message:
    def __init__(self, sender, msg_val, received, dislikes=0):
        self.sender = sender
        self.msg_val = msg_val
        self.__received = received
        self.__dislikes = dislikes


# --- uso ---
user1 = User("Juan", "1234", "juan@mail.com")
user2 = User("Ana", "5678", "ana@mail.com")

post = user1.create_post("Hola Mundo")

comment = Comment("Nice post!", author=user2)
post.add_comment(comment)

print(f"{comment.author.username} commented: {comment.comm_val}")