#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # Iterate through each row in the matrix
    for row in matrix:
        # Iterate through each element in the row
        for element in row:
            # Use str.format() to print each element without casting it into a string
            # Separate elements by space and ensure they are right-aligned with width 2
            print("{:d}".format(element), end=" ")
        # Print a new line after each row
        print()
