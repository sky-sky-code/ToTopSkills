from fastapi import FastAPI
from datetime import datetime
import uvicorn
import asyncio

app = FastAPI()


async def func1():
    print("start 1")
    await asyncio.sleep(1)
    print('end 1')


async def func2():
    print("start 2")
    await asyncio.sleep(2)
    print('end 2')


@app.get('/')
async def index():
    start_time = datetime.now()
    task_1 = asyncio.create_task(func1())
    task_2 = asyncio.create_task(func2())

    await task_1
    await task_2

    return f'Hello World {datetime.now() - start_time}'


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=80)
