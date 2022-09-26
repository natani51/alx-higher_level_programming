#!/usr/bin/python3
"""Module for add_Attribute method"""


def add_attribute(obj, name, value):
    """Method that tests if it can add an attribute"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
