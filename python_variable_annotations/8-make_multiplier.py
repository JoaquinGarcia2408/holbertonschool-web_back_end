#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier that takes a float"""
from typing import List, Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    "takes a float multiplier as argument and returns multiplies"
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
