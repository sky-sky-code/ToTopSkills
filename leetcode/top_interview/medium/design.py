import random


class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def search(self, val):
        return val in self.map

    def insert(self, val: int) -> bool:
        if self.search(val):
            return False

        self.arr.append(val)
        self.map[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.search(val):
            return False

        index = self.map[val]

        self.arr[index] = self.arr[-1]
        self.map[self.arr[-1]] = index
        self.arr.pop()
        del self.map[val]
        return True

    def get_random(self) -> int:
        return random.choice(self.arr)
