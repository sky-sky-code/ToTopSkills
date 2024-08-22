"""
Модели Конкурентности
"""
import itertools
import time
from threading import Thread, Event


def spin(msg: str, done: Event):
    for char in itertools.cycle(r'\|/-'):
        status = f'{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
        blanks = ' ' * len(status)
        print(f'\r{blanks}\r', end='')


def slow() -> int:
    time.sleep(3)
    return 43


def supervisor():
    done = Event()
    spinner = Thread(target=spin, args=('thinking', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def main():
    result = supervisor()
    print(f'Answer: {result}')


"""
тот же код на Процесах
"""

import itertools
import time
from multiprocessing import Process, Event
from multiprocessing import synchronize


def spin_v2(msg: str, done: synchronize.Event):
    for char in itertools.cycle(r'\|/-'):
        status = f'{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
        blanks = ' ' * len(status)
        print(f'\r{blanks}\r', end='')


def slow_v2() -> int:
    time.sleep(3)
    return 43


def supervisor_v2():
    done = Event()
    spinner = Process(target=spin, args=('thinking', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result


def main_v2():
    result = supervisor()
    print(f'Answer: {result}')


"""
метод async
"""
import asyncio


async def spin3(msg: str):
    for char in itertools.cycle(r'\|/-'):
        status = f'{char} {msg}'
        print(status, end='', flush=True)
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
        blanks = ' ' * len(status)
        print(f'\r{blanks}\r', end='')


async def slow3():
    time.sleep(3)
    return 43


async def supervisor3():
    spinner = asyncio.create_task(spin3(msg='thinking'))
    print(f'spinner object: {spinner}')
    result = await slow3()
    spinner.cancel()
    return result


def main3():
    result = asyncio.run(supervisor3())
    print(f'Answer: {result}')


if __name__ == '__main__':
    main3()
