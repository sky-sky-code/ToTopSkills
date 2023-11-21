import asyncio

# async def generate(n):
#     await asyncio.sleep(n)
#     print(f'Корутина generate с аргументом {n}')
#
#
# async def main():
#     tasks = [asyncio.create_task(generate(n)) for n in reversed(range(10))]
#     await asyncio.gather(*tasks)
#
#
# asyncio.run(main())

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}

counter = {'Counter 1': 0, 'Counter 2': 0, 'Counter 3': 0}

async def gencounter(couter, delay):
    for tsleep in range(max_counts[couter]):
        counter[couter] += 1
        print(f"{couter}: {counter[couter]}")
        await asyncio.sleep(delay=delay)


async def main():
    task1 = asyncio.create_task(gencounter('Counter 1', delays['Counter 1']))
    task2 = asyncio.create_task(gencounter('Counter 2', delays['Counter 2']))
    task3 = asyncio.create_task(gencounter('Counter 3', delays['Counter 3']))
    # await task1
    # await task2
    # await task3
#
asyncio.run(main())

import asyncio
#
# import asyncio
#
# async def print_message():
#     while True:
#         print("Имитация работы функции")        # Выводим сообщение о работе функции
#         await asyncio.sleep(1)                  # Останавливаем функцию на 1 секунду
#
# async def interrupt_handler(interrupt_flag):
#     print('in handler')
#     while True:
#         print('in handler loop')
#         await asyncio.sleep(0.5)                # Останавливаем функцию на 0.5 секунды
#         if interrupt_flag.is_set():             # Если interrupt_flag установлен
#             print("Произошло прерывание!, в этом месте может быть установлен любой обработчик")# Выводим сообщение о прерывании
#             interrupt_flag.clear()              # Очищаем interrupt_flag
#             break                               # Выходим из цикла
#
# async def main():
#     interrupt_flag = asyncio.Event()               # Создаем флаг interrupt_flag с помощью asyncio.Event
#     task1 = asyncio.create_task(print_message())   # Создаем задачу task1 исполняющую функцию print_message
#     task2 = asyncio.create_task(interrupt_handler(interrupt_flag)) # Создаем задачу task2 исполняющую функцию interrupt_handler с interrupt_flag в качестве аргумента
#     while True:
#         print('cплю')
#         await asyncio.sleep(3)                      # Останавливаем функцию на 3 секунды
#         interrupt_flag.set()                        # Устанавливаем interrupt_flag
#         await task2                                 # Ожидаем завершения task2
#         task2 = asyncio.create_task(interrupt_handler(interrupt_flag))  # Создаем новую задачу task2 с interrupt_flag в качестве аргумента
#
# asyncio.run(main())