# in this task, ill be wriring a python function to check whether a given input string is palindrome or not.

# a string is palindrome if A palindrome is a word, phrase, or sequence that reads the same backward as forward (ignoring case and spaces).

# Example:
# Input: "radar"
# Output: True

# Input: "hello"
# Output: False

def is_palindrome(s):
    # Remove spaces, convert to lowercase, and remove punctuation
    s = ''.join(char.lower() for char in s if char.isalnum())
    # Compare the cleaned string with its reversed version
    return s == s[::-1]

# test the function

# Ask the user for input
user_input = input("Enter a string to check if it's a palindrome: ")

# Check and display the result
if is_palindrome(user_input):
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome.")
