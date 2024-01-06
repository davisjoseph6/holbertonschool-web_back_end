#!/usr/bin/env python3
""" function make_multiplier takes a float multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Write a type-annotated function make_multiplier that takes a float
    multiplier as argument and returns a function that multiplies a float
    by multiplier """
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
