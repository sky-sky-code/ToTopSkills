"""
РЕАЛИЗАЦИЯ ПАТТЕРНОВ
ПРОЕКТИРОВАНИЯ С ПОМОЩЬЮ
ПОЛНОПРАВНЫХ ФУНКЦИЙ
"""

"""
функций как полноправных объектов
Python. Идея в том, что функции можно присваивать переменным, передавать
другим функциям, сохранять в структурах данных, а также получать атрибуты
функций, что позволяет каркасам и инструментальным средствам принимать
те или иные решения.
"""

"""
Реализация паттерна СТРАТЕГИЯ
"""

from abc import ABC, abstractmethod
from collections.abc import Sequence
from decimal import Decimal
from typing import NamedTuple, Optional, Callable


class Customer(NamedTuple):
    name: str
    fidelity: int


class LineItem(NamedTuple):
    product: str
    quantity: int
    price: Decimal

    def total(self) -> Decimal:
        return self.price * self.quantity


class Order(NamedTuple):
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional['Promotion']

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'


class Promotion(ABC):  # Стратегия: абстрактный базовый класс
    @abstractmethod
    def discount(self, order: Order) -> Decimal:
        """Вернуть скидку в виде положительной суммы в долларах"""


class FidelityPromo(Promotion):  # первая wконкретная стратегия
    """5%-ная скидка для заказчиков, имеющих не менее 1000 баллов лояльности"""

    def discount(self, order: Order) -> Decimal:
        rate = Decimal('0.05')
        if order.customer.fidelity >= 1000:
            return order.total() * rate
        return Decimal(0)


class BulkItemPromo(Promotion):  # вторая конкретная стратегия
    # «»»10%-ная скидка для каждой позиции LineItem, в которой заказано
    # не менее 20 единиц»»»
    def discount(self, order: Order) -> Decimal:
        discount = Decimal(0)
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * Decimal('0.1')
        return discount


class LargeOrderPromo(Promotion):  # третья конкретная стратегия
    """7%-ная скидка для заказов, включающих не менее 10 различных позиций"""

    def discount(self, order: Order) -> Decimal:
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * Decimal('0.07')
        return Decimal(0)


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

cart = (LineItem('banana', 4, Decimal('.5')), LineItem('apple', 10, Decimal('1.5')),
        LineItem('watermelon', 5, Decimal(5)))
Order(joe, cart, FidelityPromo())

banana_cart = (LineItem('banana', 30, Decimal('.5')), LineItem('apple', 10, Decimal('1.5')))
Order(joe, banana_cart, BulkItemPromo())

"""
ФУНКЦИОНАЛЬНО-ОРИЕНТИРОВАННАЯ СТРАТЕГИЯ
"""


class Order(NamedTuple):
    customer: Customer
    cart: Sequence[LineItem]
    promotion: Optional[Callable[['Order'], Decimal]] = None

    def total(self) -> Decimal:
        totals = (item.total() for item in self.cart)
        return sum(totals, start=Decimal(0))

    def due(self) -> Decimal:
        if self.promotion is None:
            discount = Decimal(0)
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        return f'<Order total: {self.total():.2f} due: {self.due():.2f}>'


def fidelity_promo(order: Order) -> Decimal:
    """5%-ная скидка для заказчиков, имеющих не менее 1000 баллов лояльности"""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


def bulk_item_promo(order: Order) -> Decimal:
    """10%-ная скидка для каждой позиции LineItem, в которой заказано
     не менее 20 единиц"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


#######################################################################################################################

"""
ПАТТЕРН СТРАТЕГИЯ, ДОПОЛНЕННЫЙ ДЕКОРАТОРОМ
"""

Promotion = Callable[[Order], Decimal]
promos: list[Promotion] = []


def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo


def best_promo(order: Order):
    return max(promo(order) for promo in promos)


@promotion
def fidelity(order: Order) -> Decimal:
    """5%-ная скидка для заказчиков, имеющих не менее 1000 баллов лояльности"""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


@promotion
def bulk_item_promo(order: Order) -> Decimal:
    """10%-ная скидка для каждой позиции LineItem, в которой заказано
     не менее 20 единиц"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


@promotion
def large_order(order: Order) -> Decimal:
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)

