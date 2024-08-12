#!/usr/bin/env python

import asyncio
import json
import ssl

import websockets
import uuid

headers = {"Authorization": 'Token16 eGS3jldniAkTYS9l'}


async def send_message():
    uri = f"ws://127.0.0.1:8000/ws/chat/{uuid.uuid4()}/message/send/"
    async with websockets.connect(uri=uri, extra_headers=headers, timeout=120, close_timeout=120) as websocket:
        greeting = await websocket.recv()
        print(f"<<< {greeting}")


async def chat_messages():
    uri = f"ws://127.0.0.1:8000/ws/chat/{uuid.uuid4()}messages/"
    async with websockets.connect(uri=uri, headers=headers, timeout=120, close_timeout=120) as ws:
        pass


if __name__ == "__main__":
    asyncio.run(send_message())
