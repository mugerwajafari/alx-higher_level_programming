#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all occurrences of 'c' and 'C' from the input string.

    Parameters:
    my_string (str): The input string from which 'c' and 'C' are removed.

    Returns:
    str: The modified string with 'c' and 'C' removed.
    """
    new_str = ''

    for i in my_string:
        if i not in ('C', 'c'):  # Using 'not in' for better readability
            new_str += i

    return new_str

