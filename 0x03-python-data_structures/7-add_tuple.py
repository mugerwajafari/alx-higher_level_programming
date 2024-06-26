#!/usr/bin/python3

def add_tuples(tuple1, tuple2):
    # Check if the tuples have the same length
    if len(tuple1) != len(tuple2):
        return None  # Return None if tuples have different lengths
    
    # Add corresponding elements of the tuples
    result = tuple1
    for i in range(len(tuple1)):
        result = result[:i] + (result[i] + tuple2[i],) + result[i+1:]
    return result
