def hello():
    print('Hello World')


def hello_v2():
    print('Hello World V2')


class Author:
    def __init__(self, name):
        self.name = name


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = Author(author)
