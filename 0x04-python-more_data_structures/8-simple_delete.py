def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

# Example usage
my_dictionary = {'apple': 5, 'banana': 3, 'cherry': 7}
print("Original dictionary:", my_dictionary)

# Deleting the key 'banana'
updated_dictionary = simple_delete(my_dictionary, key='banana')
print("Updated dictionary after deleting 'banana':", updated_dictionary)

# Deleting a key that doesn't exist
updated_dictionary = simple_delete(my_dictionary, key='grape')
print("Updated dictionary after deleting 'grape':", updated_dictionary)

# Deleting without specifying a key (won't delete anything)
updated_dictionary = simple_delete(my_dictionary)
print("Updated dictionary without specifying a key:", updated_dictionary)
