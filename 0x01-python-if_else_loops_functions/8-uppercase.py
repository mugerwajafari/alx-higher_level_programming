#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        if char.isalpha():  # Check if the character is an alphabet letter
            result += "{:s}".format(chr(ord(char) - 32))
        else:
            result += "{:s}".format(char)  # Add non-alphabet characters as is
    print("{}".format(result), end="")  # Print the final result without a newline
    print()
