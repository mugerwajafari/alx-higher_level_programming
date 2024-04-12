#!/usr/bin/python3

# Taking user input for two numbers

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))


def add(a, b):
    return a + b


result = add(a, b)
print("The sum of", a, "and", b, "is:", result)
