#!/usr/bin/python3
# Print numbers from 0 to 98 in decimal and hexadecimal using one print function with string format and one loop

for i in range(99):
    print("{:d} {}".format(i, hex(i)), end=' ')

# Output will be like:
# 0 0x0 1 0x1 2 0x2 3 0x3 ... 98 0x62

