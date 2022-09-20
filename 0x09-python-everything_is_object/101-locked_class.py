#!/usr/bin/python3

"""
File: 101-locked_class.py
Desc: This module contains a single class defination.
Author: natnael endale
Date Created: sep 20, 2022
"""


class LockedClass():
    """
    This class prevents the user from dynamically creating
    new instance attributes, except if the new instance
    attribute is called first_name
    """
    __slots__ = ["first_name"]
