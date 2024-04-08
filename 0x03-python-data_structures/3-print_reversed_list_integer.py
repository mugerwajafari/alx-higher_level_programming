#!/bin/python3
'''
Write a function that prints all integers of a list, in reverse order.
Prototype: def print_reversed_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers
Solution: 3-print_reversed_list_integer.py
'''
def print_reversed_list_integer(my_list=[]):
    if len(my_list) > 0:
        for num in reversed(my_list):
            print("{:d}".format(num))

my_list=[7, 9, 0, 87, 6]
result = print_reversed_list_integer(my_list)
print(result)


