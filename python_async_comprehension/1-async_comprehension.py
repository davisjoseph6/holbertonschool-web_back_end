#!/usr/bin/env python3
""" coroutine called async_comprehension"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """return list of 10 numbers using async comprehensions """
    return [i async for i in async_generator()]
