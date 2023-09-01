#!/usr/bin/env python3
"task 0: Async Generator"
import asyncio
import random


async def async_generator():
    "The coroutine will loop 10 times, each time asynchronously wait 1 second"
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
