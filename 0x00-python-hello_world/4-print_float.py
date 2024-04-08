#!/usr/bin/python3
#allow user insert number
number = input("Please enter number:")
#convert to float fomart
try:
    number = float(number)
    print("you entered:", number)
            #write to 2dp
except ValueError:
    print("Invalid input. Please enter a valid number.")
    print("Float: {:.2f}".format(number))


