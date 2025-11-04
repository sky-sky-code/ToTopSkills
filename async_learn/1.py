import asyncio
from datetime import datetime
from typing import Generator, TypeVar, Generic

CORO_RETURN_TYPE = TypeVar("ReturnType")
Coro = Generator[None, None, CORO_RETURN_TYPE]


class EventLoop:
    tasks: list["Task[CORO_RETURN_TYPE]"] = []

    @staticmethod
    def run(entry: Coro[CORO_RETURN_TYPE]) -> CORO_RETURN_TYPE:
        task: Task = EventLoop.create_task(entry)  # точку входа в пул
        while EventLoop.tasks:
            for task in EventLoop.tasks[:]:  # для безопасного удаления
                task.wake()  # пробуждаем... что-то...
                if task.done:  # удалим задачу если она завершила работу
                    EventLoop.tasks.remove(task)
        return task.result  # вернём результат нашему синхронному коду

    @staticmethod
    def create_task(coroutine: Coro[CORO_RETURN_TYPE]) -> "Task[CORO_RETURN_TYPE]":
        task: Task[CORO_RETURN_TYPE] = Task(coroutine)
        EventLoop.tasks.append(task)
        return task

    @staticmethod
    def gather(*tasks: "Task[CORO_RETURN_TYPE]") -> Coro[tuple[CORO_RETURN_TYPE, ...]]:
        while any(not task.done for task in tasks):
            yield
        return tuple(task.result for task in tasks)


class Task(Generic[CORO_RETURN_TYPE]):

    def __init__(self, coroutine: Coro[CORO_RETURN_TYPE]) -> None:
        self.coroutine: Coro[CORO_RETURN_TYPE] = coroutine
        self.done: bool = False
        self.result: CORO_RETURN_TYPE | None = None
        self.error: BaseException | None = None

    def wake(self) -> None:
        try:
            next(self.coroutine)  # делаем шаг
        except StopIteration as err:  # приехали
            self.done = True
            self.result = err.value
        except BaseException as err:  # любое возникшее исключение
            self.done = True
            self.error = err.__class__

    def wait(self) -> Coro[CORO_RETURN_TYPE]:
        while not self.done:
            yield
        return self.result


def sleep(seconds: float = 0.0) -> Coro[None]:
    start_time: datetime = datetime.now()
    while (datetime.now() - start_time).total_seconds() < seconds:
        yield


def worker(name: str) -> Coro[None]:
    print(f"{name}: приступил к работе")
    for i in sleep(10):
        yield i
    # yield from sleep(10)  # аналогично await asyncio.sleep(10)
    print(f"{name}: завершил работу")


def main() -> Coro[None]:
    print('main начал')
    for i in range(100):
        EventLoop.create_task(worker(f"Работник {i}"))
    yield
    print('main закончил')# main всё также должна возвращать генератор


EventLoop.run(main())
