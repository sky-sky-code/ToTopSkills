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


asyncio.run(main())
