#!/bin/python3
'''Write a function that computes the square value of all integers of a matrix.

Prototype: def square_matrix_simple(matrix=[]):
matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops, map, etc.
Solution: 0-square_matrix_simple.py
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''
'''have the matrix
know size
access the row
access the integer per row
square it
store in new place
go to next value square new store
'''
#have the matrix ans know the rows
'''def square_matrix_simple(matrix=[]):
    for i_m in range(len(matrix)):
        row = [matrix[i_m]]
        squared_row = [i_r**2 for i_r in row]
        print("row", i_m+1, ':', row)
         print("row", i_m + 1, ':', squared_row)
    print("no more rows")
    #access the integer per row
'''
def square_matrix_simple(matrix=[]):
    for i_m in range(len(matrix)):
        row = matrix[i_m]  # Fix: Get the row from the matrix
        squared_row = [x ** 2 for x in row]  # Square each element in the row
        print("row", i_m + 1, ':', squared_row)

    print("no more rows")

# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

square_matrix_simple(matrix)
