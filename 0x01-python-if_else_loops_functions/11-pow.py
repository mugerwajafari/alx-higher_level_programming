#!/usr/bin/python3

# Taking user input for two numbers

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))


def pow(a, b):
    return a**b


result = pow(a, b)
print(a, "power", b, "is:", result)
