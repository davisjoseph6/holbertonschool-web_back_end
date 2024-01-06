#!/usr/bin/env python3
""" Annotate the below function’s parameters and return values """
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return values with the appropriate types """
    return [(i, len(i)) for i in lst]
