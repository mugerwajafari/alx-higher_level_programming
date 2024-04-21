#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True  # Return True if value is successful
    except (ValueError, TypeError):
        return False 
