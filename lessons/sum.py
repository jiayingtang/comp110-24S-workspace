"""Summing the elements of a list using different loops."""

__author__ = "730621008"


def w_sum(vals: list[float]) -> float:
    """Sum the elements of a list using a while loop."""
    index = 0
    total = 0.0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Sum the elements of a list using a for loop without range."""
    total = 0.0
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """Sum the elements of a list using a for loop with range."""
    total = 0.0
    for index in range(len(vals)):
        total += vals[index]
    return total