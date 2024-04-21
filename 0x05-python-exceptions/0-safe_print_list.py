#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # Initialize a variable to count the number of elements printed
    count = 0
    
    # Iterate through the list using try/except
    for i in range(x):
        try:
            # Print the element at index i
            print(my_list[i],end=" ")
            # Increment the count of printed elements
            count += 1
        except IndexError:
            # If index i is out of range, break the loop
            break
    
    # Print a new line after printing all elements
    print()
    
    # Return the real number of elements printed
    return count
