#!/usr/bin/env python3
""" coroutine called measure_runtime"""
import asyncio
import time
from typing import List
from asyncio.tasks import Task

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ runtime for four parallel comprehensions """
    start_time = time.time()
    tasks: List[Task] = [asyncio.create_task(async_comprehension())
                         for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time
