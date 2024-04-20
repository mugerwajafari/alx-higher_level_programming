#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Loop through the list using index-based iteration
    for i in range(len(my_list)):
        # Check if the current element matches the search element
        if my_list[i] == search:
            # Replace the element with the new value
            my_list[i] = replace
    return my_list
