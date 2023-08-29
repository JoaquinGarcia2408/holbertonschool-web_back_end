#!/usr/bin/env python3
"task 1: Let's execute multiple coroutines at the same time with async"
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    "ou will spawn wait_random n times with the specified max_delay."
    list_floats = []
    for i in range(n):
        delay =  await (wait_random(max_delay))
        list_floats.append(delay)
    return sorted(list_floats)
