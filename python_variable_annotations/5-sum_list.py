#!/usr/bin/env python3
"""Write a type-annotated function sum_list which takes a list input_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    "takes a list input_list of floats as argument and returns their sum "
    sum: float = 0
    for number in input_list:
        sum = sum + number
    return sum
