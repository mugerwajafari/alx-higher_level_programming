#!/bin/python3
def search_replace(my_list, search, replace):
    # Loop through the list using index-based iteration
    for i in range(len(my_list)):
        # Check if the current element matches the search element
        if my_list[i] == search:
            # Replace the element with the new value
            my_list[i] = replace
    # Return the modified list
    return my_list

# Example usage
my_list = [1, 2, 3, 4]
search = 2
replace = 8
# Call the function and print the modified list
print(search_replace(my_list, search, replace))

