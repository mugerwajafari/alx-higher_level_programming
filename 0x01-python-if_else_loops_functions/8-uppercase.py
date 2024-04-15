#!/usr/bin/python3

def uppercase(s):
    for char in s:
        print("{:s}".format(chr(ord(char) - 32)), end='')
    print()
