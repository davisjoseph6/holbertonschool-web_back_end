#!/usr/bin/env python3
"""pagination"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and an end index"""

    last = page_size * page
    first = (page - 1) * page_size
    return (first, last)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset"""
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        pages = index_range(page, page_size)
        self.dataset()
        return self.__dataset[pages[0]: pages[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ returns a dictionary containing the following key-value pairs"""

        """checking next page """
        if page + 1 > len(self.dataset()):
            next_page = None
        else:
            next_page = page + 1

        """checking next page """
        if page - 1 < 1:
            prev_page = None
        else:
            prev_page = page - 1

        return ({'page_size': page_size,
                'page': page,
                 'data': self.get_page(page, page_size),
                 'next_page': next_page,
                 'prev_page': prev_page,
                 'total_pages': len(self.dataset())
                 })