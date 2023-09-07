#!/usr/bin/env python3
"task 0: Simple helper function"


def index_range(page, page_size):
    "start index and an end index corresponding to the range of indexes"
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    return (start_index, end_index)
