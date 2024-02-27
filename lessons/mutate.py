"""Mutating functions."""

__author__ = "730621008"


def manual_append(numbers: list[int], number: int) -> None:
    """Appends an int to the end of a list of ints.

    Args:
    numbers: list of integers to be appended to.
    number: the integer to append to the list.
    """
    numbers.append(number)


def double(numbers: list[int]) -> None:
    """Doubles every element in a list of ints.

    Args:
    numbers: list of integers to be doubled.
    """
    for i in range(len(numbers)):
        numbers[i] *= 2