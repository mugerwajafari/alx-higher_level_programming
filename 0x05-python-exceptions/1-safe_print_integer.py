#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Try to format the value as an integer and print it
        print("{:d}".format(value))
        return True  # Return True if value is successfully printed
    except (ValueError, TypeError):
        return False  # Return False if value cannot be formatted as an integer or if an error occurs

# Test cases
print(safe_print_integer(42))  # Output: 42 (followed by a new line), True
print(safe_print_integer("hello"))  # Output: False

