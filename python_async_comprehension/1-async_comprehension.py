#!/usr/bin/env python3
"task 1: Async Comprehensions"
import asyncio
import random
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    "then return the 10 random numbers."
    random_numbers = [number async for number in async_generator()]
    return random_numbers
