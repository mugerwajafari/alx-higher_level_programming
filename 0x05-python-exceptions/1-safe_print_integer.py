#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True  # Return True if value is successfully printed
    except (ValueError, TypeError):
        return False  # Return False if value cannot be formatted as an integer or if an error occurs
