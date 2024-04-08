#!/bin/python3
def common_elements(set_1, set_2):
    answer = set()  # Initialize an empty set for common elements
    for item in set_1:
        if item in set_2:
            answer.add(item)  # Add common elements to the answer set
    return answer

set_1 = {1, 4, 8, 86, 6}  # Define sets using curly braces for set literals
set_2 = {1, 8, 6, 5, 89}

print(common_elements(set_1, set_2))

