#!/usr/bin/python3
"""Documentation for a square printing function"""


def print_square(size):
    """Prints a square of length size"""

    if isinstance(size, int):
        if size >= 0:
            for i in range(size):
                [print('#', end='') for i in range(size)]
                print()
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
