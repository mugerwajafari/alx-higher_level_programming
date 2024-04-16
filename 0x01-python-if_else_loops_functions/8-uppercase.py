#!/usr/bin/python3

def uppercase(s):
    """Convert to uppercase."""
    for c in s:
        ch = ord(c)
        if ch >= 97 and ch <= 122:
            ch -= 32
        print("{}".format(chr(ch)), end="")
    print()
