from collections import namedtuple
from dataclasses import dataclass, field
from typing import NamedTuple

Coordinate = namedtuple('Coordinate', 'lat lon')


@dataclass(frozen=type)
class Coordinate:
    lat: float
    lon: float

    def __str__(self):
        ns = 'N' if self.lat >= 0 else 'S'
        we = 'E' if self.lon >= 0 else 'W'
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'


@dataclass
class ClubMember:
    name: str
    guests: list = field(default_factory=list)


class RegularBook:
    def __init__(self, title, author):
        self.title = title
        self.author = author

        # ||
        # \/


@dataclass
class Book:
    title: str
    author: str
