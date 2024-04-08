'''
Write a function that replaces an element of a list at a specific position (like in C).

Prototype: def replace_in_list(my_list, idx, element):
If idx is negative, the function should not modify anything, and returns the original list
If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
You are not allowed to import any module
You are not allowed to use try/except
Solution: 2-replace_in_list.py
'''
def replace_in_list(my_list, idx, element):
    if (idx < 0):
      return my_list
    elif (idx >= len(my_list)):
      return my_list
   # element replacement
    my_list[idx] = element
    return my_list
my_list = [8, 80, 5, 6,4]
idx = 0
element = 100
results = replace_in_list(my_list, idx, element)
print (results)
