#!/usr/bin/python3
"""Module that provides a function that adds to ints."""


def add_integer(a, b=98):
    """Adds two integers.
    Args:
        a (int, float): first number to add.
        b (int, float): second number to add.
    Raises:
        TypeError: if a or b is not an integer or float.
    Returns:
        int: the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
