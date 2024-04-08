#!/bin/bash/python3
def only_diff_elements(set_1, set_2):
    answer = set()  # Initialize an empty set for common elements
    for item in set_1:
        if item in set_2:
            answer= set_1 ^ set_2 # sort out the different items
            #answer.add(item)  # Add common elements to the answer set
    return answer

set_1 = {1, 4, 8, 86, 6}  # Define sets using curly braces for set literals
set_2 = {1, 8, 6, 5, 89}

print(only_diff_elements(set_1, set_2))

