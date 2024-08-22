"""
Когда python выполняет декораторы
Главное свойство декораторов – то, что они выполняются сразу после определения декорируемой функции
"""
import time

registry = []


def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func


@register
def f1():
    print('running f1')


@register
def f2():
    print('running f2')


def f3():
    print('running f3')


def main():
    print('running main()')
    print('registry -> ', registry)
    f1()
    f2()
    f3()


def clock(func):
    """
    пример того, что start выполнения будет отчитывваться сразу после определения декорирующей функции
    """
    print('В декораторе')
    start = time.perf_counter()

    def clocked(*args, **kwargs):
        result = func(*args, **kwargs)
        finish = time.perf_counter() - start
        print(f'я выполнился: fun = {result} time: = {finish}')

    return clocked


@clock
def summ(a, b):
    return a + b


#######################################################################################################################


def make_averager():
    """--------------------------------"""  # Замыкаие
    series = []

    def averager(new_value):
        series.append(new_value)  # свободная переменная
        total = sum(series)
        return total / len(series)

    """---------------------------------"""
    return averager


avg = make_averager()
print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)

"""
series – локальная переменная make_averager, потому
что инициализация series = [] производится в теле этой функции. Но к моменту вызова avg(10)
функция make_averager уже вернула управление, и ее локальная область видимости уничтожена. 

НО замыкание – это функция, которая запоминает привязки свободных переменных, существовавшие на момент определения функции, так
что их можно использовать впоследствии при вызове функции, когда область
видимости, в которой она была определена, уже не существует
"""

"""
На самом деле декорируемая функция заменяется новой, которая принимает такие же аргументы и как правило возрващает
то что должна вернуть декорируемая функция, но при этом произвести доп действия
"""

import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0

        name = func.__name__
        arg_lst = [repr(arg) for arg in args]
        arg_lst.extend(f'{k}={v!r}' for k, v in kwargs.items())
        arg_str = ', '.join(arg_lst)
        print(f'[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}')
        return result

    return clocked


"""
ЗАПОМИНАНИЕ С ПОМОЩЬЮ FUNCTOOLS.CACHE
"""

from functools import cache


@cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    print(fibonacci(6))

"""
ОБОБЩЕННЫЕ ФУНКЦИИ С ОДИНОЧНОЙ ДИСПЕТЧЕРИЗАЦИЕЙ
"""
"""
Мы  хотим, чтобы он умел генерировать HTML-представления объектов Python разного типа.
"""

import html

"""
она будет работать только для одного типа
декоратор singledispatch решает эту проблему
"""
#
# def htmlize(obj):
#     content = html.escape(repr(obj))
#     return f'<pre>{content}</pre>'


from functools import singledispatch
from collections import abc
import decimal
import fractions
import numbers


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'


@htmlize.register
def _(text: str) -> str:
    content = html.escape(text).replace('\n', '<br/>\n')
    return f'<p>{content}</p>'


@htmlize.register
def _(seq: abc.Sequence):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


@htmlize.register
def _(n: numbers.Integral) -> str:
    return f'<pre>{n} (0x{n:x})</pre>'


@htmlize.register
def _(n: bool) -> str:
    return f'<pre>{n}</pre>'


@htmlize.register(fractions.Fraction)
def _(x) -> str:
    frac = fractions.Fraction(x)
    return f'<pre>{frac.numerator}/{frac.denominator}</pre>'


"""
ПАРАМЕТРИЗОВАННЫЙ РЕГИСТРАЦИОННЫЙ ДЕКОРАТОР

Чтобы функцию регистрации, вызываемую декоратором register, можно было
активировать и деактивировать, мы снабдим ее необязательным параметром
active: если он равен False
"""

registry = set()


def register(active=True):
    def decor(func):
        print('running register' f'(active={active})->decorate({func})')
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func

    return decor


@register(active=False)
def f1():
    print('running f1()')


"""
ДЕКОРАТОР CLOCK НА ОСНОВЕ КЛАССА
"""

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


class clock:

    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result

        return clocked


@clock()
def func_sum():
    return 10 + 10
