#!/usr/bin/python3
import random

# Generate a random number
number = random.randint(-10000, 10000)

# Calculate the last digit
lastDigit = abs(number) % 10

# if the last digit is greater than 5: the string > 5
if lastDigit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lastDigit))

# if the last digit is 0: the string and is 0
if lastDigit == 0:
    print("Last digit of {} is {} and is 0".format(number, lastDigit))

if number < 0:
    last_digit = ((number * -1) % 10) * -1
# if the last digit is< 6 and != 0: the string is< 6 & !0
if lastDigit < 6 and lastDigit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, lastDigit))
