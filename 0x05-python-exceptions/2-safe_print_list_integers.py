#!/usr/bin/python3
'''Write a function that prints the first x elements of a list and only integers.

Prototype: def safe_print_list_integers(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
x represents the number of elements to access in my_list
x can be bigger than the length of my_list - if it’s the case, an exception will occur
Returns the real number of integers printed
You have to use try: / except:
You have to use "{:d}".format() to print an integer
You are not allowed to import any module
You are not allowed to use len()
Solution: 2-safe_print_list_integers.py'''

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int and printed != x:
                print('{:d}'.format(my_list[i]), end='')
                printed += 1

        except TypeError:
            continue
    print()

    return printed

# Example usage:
my_list = [1, 2, 3, 'four', 5, 'six', 7]
x = 5
print("Number of integers printed:", safe_print_list_integers(my_list, x))
