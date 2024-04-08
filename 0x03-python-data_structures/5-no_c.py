#!/bin/python3

def no_c(my_string):
    # Ensure the code contains c
    if 'c' in my_string.lower() or 'C' in my_string:
        # Prompt for the new letter
        new_letter = input("Enter the letter to replace 'c' and 'C' with: ")
        # Replace 'c' and 'C' with the new letter
        new_string = ''
        for char in my_string:
            if char != 'c' and char != 'C':
                new_string += char
            else:
                new_string += new_letter
        return new_string
    else:
        return "The word does not contain the letter 'c' or 'C'."

my_string = input("Enter a word with 'c' or 'C': ")
answer = no_c(my_string)
print("The new word is:", answer)

