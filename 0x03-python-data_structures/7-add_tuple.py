#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuplen1 = len(tuple_a)
    tuplen2 = len(tuple_b)

    if tuplen1 < 2 and tuplen1 == 1:
        tuple_a = (tuple_a[0], 0)
    if tuplen1 < 2 and tuplen1 == 0:
        tuple_a = (0, 0)
    if tuplen2 < 2 and tuplen2 == 1:
        tuple_b = (tuple_b[0], 0)
    if tuplen2 < 2 and tuplen2 == 0:
        tuple_b = (0, 0)
    tuple_c = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return tuple_c
