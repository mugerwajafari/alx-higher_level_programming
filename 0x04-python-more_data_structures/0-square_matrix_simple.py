#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    for i_m in range(len(matrix)):
        row = matrix[i_m]  # Fix: Get the row from the matrix
        squared_row = [x ** 2 for x in row]  # Square each element in the row
        print("row", i_m + 1, ':', squared_row)

    print("no more rows")
