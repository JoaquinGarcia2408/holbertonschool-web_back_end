#!/usr/bin/env python3
"task 1: Simple pagination"
import csv
import math
from typing import List


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
        "checks the validity of the arguments, uses index_range"
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if start_index >= len(data) or end_index <= 0:
            return []

        return data[start_index:end_index]


def index_range(page, page_size):
    "start index and an end index corresponding to the range of indexes"
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
