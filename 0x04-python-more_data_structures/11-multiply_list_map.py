#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Using map to multiply each element of the list by the given number
    multiplied_list = list(map(lambda x: x * number, my_list))
    return multiplied_list
