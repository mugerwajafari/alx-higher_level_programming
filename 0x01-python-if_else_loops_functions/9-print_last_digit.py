#!/usr/bin/python3/
#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        last_digit = number % 10
    else:
        last_digit = (-number) % 10

    print(last_digit, end='')
    return last_digit

user_input = input("Enter a number: ")
number = int(user_input)
last_digit = print_last_digit(number)
print("\nThe last digit of the number is:", last_digit)


