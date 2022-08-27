#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None

    maxNum = my_list[0]
    for num in my_list:
        if num > maxNum:
            maxNum = num

    return maxNum
