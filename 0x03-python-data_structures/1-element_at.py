#!/bin/bash/python3
'''
Write a function that retrieves an element from a list like in C.

Prototype: def element_at(my_list, idx):
If idx is negative, the function should return None
If idx is out of range (> of number of element in my_list), the function should return None
You are not allowed to import any module
You are not allowed to use try/except
'''

def element_at(my_list, idx):
    #ensuring not empty for two var
    if idx < 0 or idx >= len(my_list) :
        return "None"
    else:
        return my_list[idx]
    #checking
my_list = [10, 20, 30, 40, 50]
idx = 2
result = element_at(my_list, idx)
print(idx, result)
