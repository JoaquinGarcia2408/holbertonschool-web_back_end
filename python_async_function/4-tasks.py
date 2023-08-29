#!/usr/bin/env python3
"""task 4: Tasks"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    task = []
    for i in range(n):
        delay = await (task_wait_random(max_delay))
        task.append(delay)
    return sorted(task)
