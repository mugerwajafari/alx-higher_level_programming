#!/usr/bin/python3

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122 and  len(c) == 1:
        return True
    else:
        return False
