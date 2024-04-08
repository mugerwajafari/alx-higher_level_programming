#!/bin/python3

'''Replace in a copy

Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

Prototype: def new_in_list(my_list, idx, element):
If idx is negative, the function should return a copy of the original list
If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
You are not allowed to import any module
You are not allowed to use try/except
Solution: 4-new_in_list.py
'''
def new_in_list(my_list, idx, element):
    copy = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return copy

    copy[idx] = element
    return copy

my_list =[6,76,5,44,7,77]
element = 100
idx = 0
result = new_in_list(my_list, idx, element)
print(result)




