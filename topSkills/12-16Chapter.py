import functools
import itertools
import operator
from array import array
import reprlib
import math

from collections.abc import Sequence, Sized


class Vector:
    typecode = 'd'

    __match_args__ = ('x', 'y', 'z', 't')

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]

        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    """
    базовый протокол последовательности: методы __len__ и __getitem__;
    
    Любому опытному программисту на Python
    достаточно одного взгляда на код, что понять, что это именно класс последовательность. Протоколы и утиная типизация  385
    в действительности, несмотря на то что он является подклассом object. Мы говорим,
    что он является последовательностью, потому что ведет себя как последовательность, а только это и важно.
    Такой подход получил название «утиная типизация», и
    """

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        """
        Вызывается при vector[0], где key 0
        """
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]

    """
    Метод __getattr__ вызывается интерпретатором, если поиск атрибута завершается неудачно.
    Python проверяет, есть ли у объекта my_obj атрибут с именем x; если нет, поиск повторяется
    в классе (my_obj.__class__), а затем вверх по иерархии наследования1.

    Python вызывает этот метод только в том случае, когда у объекта нет атрибута
    с указанным именем. Однако же после присваивания v.x = 10 у объекта v появился атрибут x,
    поэтому __getattr__ больше не вызывается для доступа к v.x: интерпретатор просто вернет значение 10
    """

    def __getattr__(self, name):
        cls = type(self)

        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1

        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        return AttributeError(msg)

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.__match_args__:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = 'cant set attributes "a" to "z" in {cls_name!r}'
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes, 0)

    """
    CHAPTER 16 ПЕРЕГРУЗКА ОПЕРАТОРОВ
    
    Перегрузка операторов позволяет определенным пользователем объектам взаимодействовать
    с инфиксными операторами, например + и |, и с унарными операторами, например - и ~
    
    Если специальный метод оператора не  может вернуть правильный результат из-за 
    несовместимости типов, он должен возвращать значение NotImplemented, а не возбуждать исключение TypeError.
    
    Это позволит интерпретатору вызвать метод инверсного оператора (__radd__), который, возможно, сумеет завершить вычисление,
    поменяв местами операндыразных типов
    """

    def __neg__(self):
        """
        возвращает отрицательный -obj(self)
        """
        return Vector(-x for x in self)

    def __pos__(self):
        """
        возваращает положительный obj
        """
        return -Vector(self)

    def __invert__(self):
        """
        ~ (реализован с помощью __invert__)
        """
        pass

    def __add__(self, other):
        """
        Обратите внимание, что __add__ возвращает новый экземпляр Vector, не изменяя ни self, ни other.
        """
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(a + b for a, b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        return Vector(n * scalar for n in self)

    __rmul__ = __mul__


vector = Vector([1, 2, 3])
print((1, 2, 3) + vector)


"""
Оператор
+        __add__       __radd__       __iadd__         Сложение или конкатенация
-        __sub__       __rsub__       __isub__         Вычитание
*        __mul__       __rmul__       __imul__         Умножение или повторение
/        __truediv__   __rtruediv__   __itruediv__     Истинное деление
//       __floordiv__  __rfloordiv__  __ifloordiv__    Деление с округлением
%        __mod__       __rmod__       __imod__         Деление по модулю
divmod() __divmod__    __rdivmod__    __idivmod__      Возвращает кортеж, содержащий частное и остаток


**,pow() __pow__       __rpow__       __ipow__         Возведение в степеньa
@        __matmul__    __rmatmul__    __imatmul__      Матричное умножение
&        __and__       __rand__       __iand__         Поразрядное И
| __or__ __ror__ __ior__                               Поразрядное ИЛИ
^ __xor__ __rxor__ __ixor__                            Поразрядное ИСКЛЮЧАЮЩЕЕ ИЛИ
<< __lshift__ __rlshift__ __ilshift__                  Поразрядный сдвиг влево
>> __rshift__ __rrshift__ __irshift__                  Поразрядный сдвиг вправо
"""
vector2 = Vector([2, 4, 5])
vector += vector2