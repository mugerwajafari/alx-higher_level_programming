#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary

# Define the dictionary 'a_dictionary'
a_dictionary = {'cow': 'moo'}

# Define the key and value to be updated
key = 'dog'
value = 'bark'

# Call the function and print the updated dictionary
print(update_dictionary(a_dictionary, key, value))
