#!/usr/bin/env python3
"""task 0: the basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    "Write an asynchronous coroutine that takes in an integer argument"
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return(delay)
