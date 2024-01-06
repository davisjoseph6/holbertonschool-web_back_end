#!/usr/bin/env python3
""" function to_kv list takes a string and a int or float
    and return a tuple """
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return a tuple with string k and square of int/float v """
    return k, v ** 2
