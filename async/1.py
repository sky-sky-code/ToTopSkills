import asyncio


async def task(name, delay):
    print(f"Запуск задачи {name}")
    await asyncio.sleep(delay)
    print(f"Завершение задачи {name}")


async def main():
    tasks = [
        asyncio.create_task(task("-Задача 1-", 1)),
        asyncio.create_task(task("-Задача 2-", 0.5)),
        asyncio.create_task(task("-Задача 3-", 2))
    ]

    await asyncio.gather(*tasks)


async def one():
    while True:
        await asyncio.sleep(1)
        try:
            asyncio.CancelledError
        except Exception as e:
            break
        print('hello')


async def slow():
    await asyncio.sleep(3)
    return 45


async def two():
    task_1 = asyncio.create_task(one())
    resul = await slow()
    task_1.cancel()
    print(resul)

asyncio.run(two())