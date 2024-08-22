class StringField:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class DataBase:
    x = StringField()
    y = StringField()

    def __init__(self, x, y):
        self.x = x
        self.y = y


db = DataBase('hi', 'low')
db.__dict__['x'] = 'top'
print(db.x)


class FloatValue:
    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue

    def __init__(self, value=0.0):
        self.value = value


class TablaSheet:

    def __init__(self, n, m):
        self.cells = [[Cell() for _ in range(n)] for _ in range(m)]


class ValidateString:

    def __init__(self, min_length=3, max_length=180):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return type(string) == str and self.min_length <= len(string) <= self.max_length


class StringValue:
    def __init__(self, validator=ValidateString()):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue()
    password = StringValue()
    email = StringValue()

    def __init__(self, login="логин", password="пароль", email="email"):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f"<form>\nЛогин: <{self.login}>\nПароль: <{self.password}>\nEmail: <{self.email}>\n</form>")


class Book:

    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if type(value) == int and key in ('pages', 'year'):
            return object.__setattr__(self, key, value)
        elif type(value) == str and key in ('title', 'author'):
            return object.__setattr__(self, key, value)
        else:
            raise "Неверный тип присваиваемых данных."


book = Book("Python ООП", "Сергей Балакирев", 123, 202)
