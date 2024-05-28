# import asyncio
#
# max_counts = {
#     "Counter 1": 13,
#     "Counter 2": 7
# }
#
# counters = {
#     'Counter 1': 0,
#     'Counter 2': 0
# }
#
#
# async def fill_counters(name_counter, delay):
#     for sec in range(1, delay + 1):
#         counters[name_counter] += sec
#         await asyncio.sleep(sec)
#         print(f'{name_counter}: {sec}')
#
#
# async def main():
#     task1, task2 = (asyncio.create_task(fill_counters('Counter 1', 13)),
#                     asyncio.create_task(fill_counters('Counter 2', 7)))
#
#     await asyncio.gather(task1, task2)
#
#
# asyncio.run(main())


def count_calls(func):
    num_calls = 0

    def wrapper(*args, **kwargs):
        nonlocal num_calls
        num_calls += 1
        print(f"Функция была вызвана {num_calls} раз(а)")
        return func(*args, **kwargs)

    return wrapper


def my_func():
    print("Hello, world!")

