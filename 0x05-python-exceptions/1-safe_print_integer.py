#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Try to format the value as an integer and print it
        print("{:d}".format(value))
        return True  # Return True if value is successfully printed
    except (ValueError, TypeError):
        return False  # Return False if value cannot be formatted as an integer or if an error occurs
