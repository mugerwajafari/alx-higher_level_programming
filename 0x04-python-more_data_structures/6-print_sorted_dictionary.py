#!/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the sorted keys of the dictionary
    sorted_keys = sorted(a_dictionary.keys())

    # Iterate through sorted keys and print key-value pairs
    for key in sorted_keys:
        # Check if the value corresponding to the key is a dictionary
        if isinstance(a_dictionary[key], dict):
            # If it's a dictionary, print its keys in the order they appear
            for sub_key in a_dictionary[key].keys():
                print(f"{sub_key}: {a_dictionary[key][sub_key]}")
        else:
            # If it's not a dictionary, print the key-value pair directly
            print(f"{key}: {a_dictionary[key]}")

# Example usage
my_dictionary = {"b": 2, "a": 1, "c": 3, "d": {"e": 5, "f": 6}}
print_sorted_dictionary(my_dictionary)
