#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # Using map to multiply each element of the list by the given number
    multiplied_list = list(map(lambda x: x * number, my_list))
    return multiplied_list

# Example usage:
original_list = [1, 2, 3, 4, 5]
multiplier = 3
print("Original list:", original_list)

result_list = multiply_list_map(original_list, multiplier)
print("Resulting list after multiplication:", result_list)

