#!/usr/bin/env python3
""" function sum_list takes a list of floats or integers """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ calculates the sum of the list """
    return sum(mxd_lst)
