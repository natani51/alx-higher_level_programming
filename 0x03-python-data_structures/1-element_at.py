#!/usr/bin/python3

def element_at(my_list, idx):
    rng = len(my_list) - 1
    if idx < 0 or idx > rng:
        pass
    else:
        return my_list[idx]
