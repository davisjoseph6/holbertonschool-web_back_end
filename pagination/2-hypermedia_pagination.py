#!/usr/bin/env python3
"""Pagination helper function"""
import csv
import math
from typing import Tuple, List, Dict, Optional


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end indices for a given page"""
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


class Server:
    """Class for server to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Retrieve and cache the dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a specific page of the dataset"""
        assert isinstance(page, int) and isinstance(page_size, int), (
            "Page and page_size must be integers"
        )
        assert page > 0, "Page must be a positive integer"
        assert page_size > 0, "Page size must be a positive integer"
        self.dataset()
        i = index_range(page, page_size)
        if i[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[i[0]:i[1]]

    def get_hyper(
            self,
            page: int = 1,
            page_size: int = 10
    ) -> Dict[str, Optional[int]]:
        """Provide hypermedia information about the dataset page"""
        data_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        hyper_dict = {
            'page_size': len(data_page),
            'page': page,
            'data': data_page,
            'next_page': page + 1 if page * page_size < len(self.__dataset)
            else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

        return hyper_dict


if __name__ == "__main__":
    # Test cases
    server = Server()

    print(server.get_hyper(1, 2))
    print("---")
    print(server.get_hyper(2, 2))
    print("---")
    print(server.get_hyper(100, 3))
    print("---")
    print(server.get_hyper(3000, 100))
