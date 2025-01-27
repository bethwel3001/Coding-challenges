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
        

# Test the function
print(find_first_non_repeating_char("swiss"))  # Output: 'w'
print(find_first_non_repeating_char("aabbcc"))  # Output: None
print(find_first_non_repeating_char("programming"))  # Output: 'p'        
        