# Problem 4: Find the First Non-Repeating Character

# Write a Python function that takes a string as input and returns the first  non-repeating character. If all characters repeat, return None.

def find_first_non_repeating_char(s):
    # Create a dictionary to store the count of each character
    char_count = {}
    
    # First pass: Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Second pass: Find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    # If all characters repeat, return None
    return None
        
# Take input from the user
user_input = input("Enter a string to find the first non-repeating character: ")

# Call the function and display the result
result = find_first_non_repeating_char(user_input)

if result:
    print(f"The first non-repeating character is: '{result}'")
else:
    print("There are no non-repeating characters in the string.")        
        