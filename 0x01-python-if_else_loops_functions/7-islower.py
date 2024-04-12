#!/usr/bin/python3

def islower(c):
    return ord(c) >= 97 and ord(c) <= 122


c = input("Enter a character: ")

if len(c) == 1:
    if islower(c):
        print("The input character is lowercase.")
    else:
        print("The input character is not lowercase.")
else:
    print("Please enter exactly one character.")
