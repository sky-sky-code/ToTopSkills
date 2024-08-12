import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


invoice = """
.........................................................
1909   Pimoroni PiBrella                $17.50   3   $52.50
1489   6mm Tactile Switch x20           $4.95    2   $9.90
1510   Panavise Jr. - PV-201            $28.00   1   $28.00
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])


def act(command):
    match command.split():
        case "Cook", "breakfast":
            return "Я люблю завтракать."
        case "Cook", *wtv:
            return f"готовится"
        case "Go", "North" | "East" | "South" | "West":
            return "Хорошо, я пошел!"
        case "Go", *wtv:
            return "Неизвестное напраление..."
        case _:
            return "Я не могу этого сделать..."


#
# print(act("Go North"))
# print(act("Go asdsd"))
# print(act("Cook breakfast"))
# print(act("Drive"))

colors = ['black', 'white']

sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)


def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'author': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]


dct = {'name': 'Sai', 'familia': 'Pash'}

dct.setdefault('parent', []).append({'name': 'P', 'fam': 'ads'})

import collections


class StrkeyDict(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


import copy


class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.remove(name)

    def drop(self, name):
        self.passengers.remove(name)


# bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
# bus2 = copy.copy(bus1)
# bus3 = copy.deepcopy(bus1)
# print(id(bus1), id(bus2), id(bus3))
# bus1.drop('Bill')
# print(bus2.passengers)
# print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))


def fac(n):
    return 1 if n < 2 else n * fac(n - 1)


list(map(fac, range(6)))
[fac(n) for n in range(6)]

import random


class BingoCage:

    def __int__(self, items):
        self._items = list(items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


def teg(name, *content, class_=None, **attrs):
    if class_ is not None:
        attrs['class'] = class_
    attr_pairs = (f'{attr}="{value}"' for attr, value in sorted(attrs.items()))
    attr_str = ''.join(attr_pairs)
    if content:
        elements = (f'<{name}{attr_str}>{c}</{name}>'
                    for c in content)
        return '\n'.join(elements)
    else:
        return f'<{name}{attr_str} />'


d1 = {1: '1', 2: 2}
d2 = {3: '3', 5: '4'}


