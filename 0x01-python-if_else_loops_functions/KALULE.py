#!/usr/bin/python3

import sys

# Get command-line arguments
arguments = sys.argv

# Print script name
print("Script name:", arguments[0])

# Print other command-line arguments
if len(arguments) > 1:
    print("Other arguments:", arguments[1:])

