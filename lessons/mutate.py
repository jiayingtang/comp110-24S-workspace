"""Mutating functions."""
__author__ = "730621008"

from typing import List

def manual_append(a: List[int], value: int) -> None:
    a.append(value)

def double(a: List[int]) -> None:
    index = 0
    while index < len(a):
        a[index] *= 2
        index += 1