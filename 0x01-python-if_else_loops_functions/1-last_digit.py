#!/usr/bin/python3
 #This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

variable_number = input("Enter variable number:")
variableNumber = int(variable_number)
print(variableNumber)
lastDigit = variableNumber % 10
#print last digit
print(lastDigit)
#if the last digit is greater than 5: the string and is greater than 5
if (lastDigit > 5):
    print("the string and is greater than 5")
#if the last digit is 0: the string and is 0
if (lastDigit == 0):
    print("the string and is 0")
#if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
if (lastDigit < 6 and lastDigit != 0):
    print("the string and is less than 6 and not 0")

