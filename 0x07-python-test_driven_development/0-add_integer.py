#!/usr/bin/python3

"""Documentation for a simple add function"""


def add_integer(a, b=98):
    """Calculates the addition of two numbers"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must an integer")
    return int(a) + int(b)
