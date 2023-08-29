#!/usr/bin/env python3
"Write a type-annotated function to_kv that takes a string and an int OR float"
from typing import Tuple, Union


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    "arguments and returns a tuple"
    tup = (k, v * v)
    return tup
