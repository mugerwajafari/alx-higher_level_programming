#!/usr/bin/python3
# ASCII values for lowercase letters range from 97 to 122
for i in range(97, 123):
    if (chr(i) != 'q' and chr(i) != 'e'):
        print(chr(i), end='')
