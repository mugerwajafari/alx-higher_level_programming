#!/usr/bin/python3

def print_reversed_list_integer(my_list=None):
    if my_list is None:
        return None

    if len(my_list) > 0:
        for num in reversed(my_list):
            print("{:d}".format(num))
    else:
        return None
