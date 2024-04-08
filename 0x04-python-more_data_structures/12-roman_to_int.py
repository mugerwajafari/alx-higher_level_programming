#!/usr/bin/python3
def roman_to_int(roman_string):
    # Check if the input is not a string or None
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    
    # Define a dictionary to map Roman numerals to their integer values
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    # Initialize the total sum
    total = 0
    
    # Iterate through the Roman numeral string
    for i in range(len(roman_string)):
        # Get the integer value of the current Roman numeral character
        value = roman_values.get(roman_string[i])
        
        # If the current character is the last one or its value is greater than or equal to the next one, add its value to the total
        if i == len(roman_string) - 1 or roman_values.get(roman_string[i + 1]) <= value:
            total += value
        # Otherwise, subtract its value (since it represents a subtraction case like IV or IX)
        else:
            total -= value
    
    return total

# Example usage:
print(roman_to_int("III"))  # Output: 3
print(roman_to_int("IX"))   # Output: 9
print(roman_to_int("LVIII")) # Output: 58
print(roman_to_int("MCMXCIV")) # Output: 1994
print(roman_to_int(None))   # Output: 0
print(roman_to_int(123))    # Output: 0
