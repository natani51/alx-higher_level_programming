#!/usr/bin/python3
"""Documenatation for a simple sy_my_name function"""


def say_my_name(first_name, last_name=""):
    """Prints the first_name and the last_name passed in"""

    if not type(first_name) == str:
        raise TypeError("first_name must be a string")
    if not type(last_name) == str:
        raise TypeError("last_name must be a string")
    print("my name is {} {}".format(first_name, last_name))
