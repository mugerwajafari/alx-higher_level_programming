#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()

    # Iterate over the key-value pairs of the copied dictionary
    for k, v in b_dictionary.items():
        b_dictionary[k] = v * 2
    return b_dictionary
