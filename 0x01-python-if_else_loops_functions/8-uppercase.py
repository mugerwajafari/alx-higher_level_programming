#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if not (ord('A') <= ord(char) <= ord('Z')):
            return False
    return True
