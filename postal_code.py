import re

# Regular expressions for validating postal code
regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

# Get user input for postal code
postal_code = input("Enter a postal code: ")

# Validate postal code using regular expressions
if re.match(regex_integer_in_range, postal_code) and not re.search(regex_alternating_repetitive_digit_pair, postal_code):
    print("Valid postal code")
else:
    print("Invalid postal code")