#!/usr/bin/python3

def islower(c):
    return ord(c) >= 97 and ord(c) <= 122


c = input("Enter a character: ")

if len(c) == 1:
    if islower(c):
        print(True)
    else:
        print(False)
else:
    print("Please enter exactly one character.")
