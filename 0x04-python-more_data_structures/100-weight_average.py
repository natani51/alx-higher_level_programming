#!/usr/bin/python3

def weight_average(my_list=[]):
    ln = len(my_list)
    if ln == 0:
        return 0
    s = 0
    di = 0
    for i in range(ln):
        s += (my_list[i][0] * my_list[i][1])
        di += my_list[i][1]
    return s / di
