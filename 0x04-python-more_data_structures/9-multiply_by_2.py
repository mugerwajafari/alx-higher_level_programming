#!/bin/python3
def multiply_by_2(a_dictionary):
    # Create a copy of the input dictionary to avoid modifying the original dictionary
    b_dictionary = a_dictionary.copy()

    # Iterate over the key-value pairs of the copied dictionary
    for k, v in b_dictionary.items():
        # Multiply each value by 2 and update the corresponding value in the copied dictionary
        b_dictionary[k] = v * 2

    # Return the modified dictionary with values multiplied by 2
    return b_dictionary

# Example usage:
original_dictionary = {'a': 1, 'b': 2, 'c': 3}
print("Original dictionary:", original_dictionary)

multiplied_dictionary = multiply_by_2(original_dictionary)
print("New dictionary with values multiplied by 2:", multiplied_dictionary)

