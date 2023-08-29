#!/usr/bin/env python3
"task 2: measure time"
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    "Create a measure_time function with integers n and max_delay as arguments"
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time
    average_time = total_time / n

    return average_time
