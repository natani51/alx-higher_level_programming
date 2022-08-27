#!/usr/bin/python3
def no_c(my_string):
    nocC = ""
    for item in my_string:
        if item == 'c' or item == 'C':
            nocC += ""
            continue
        nocC += item
    return nocC
