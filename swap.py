def swap_case(s):
    # Create an empty string to store the modified string
    result = ""
    # Loop through each character in the input string
    for c in s:
        # Check if the character is uppercase
        if c.isupper():
            # Convert it to lowercase and append to the result string
            result += c.lower()
        # Check if the character is lowercase
        elif c.islower():
            # Convert it to uppercase and append to the result string
            result += c.upper()
        # If the character is not a letter, append it to the result string as is
        else:
            result += c
    # Return the modified string
    return result

# Read the input string from the user
input_str = input().strip()

# Call the swap_case function to modify the string
modified_str = swap_case(input_str)

# Print the modified string
print(modified_str)