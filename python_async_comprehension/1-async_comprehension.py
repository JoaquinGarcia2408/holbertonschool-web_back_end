#!/usr/bin/env python3
"task 1: Async Comprehensions"
import asyncio
import random
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    "The coroutine will collect 10 random numbers using an async comprehensing over async_generator"
    random_numbers = [number async for number in async_generator()]
    return random_numbers
