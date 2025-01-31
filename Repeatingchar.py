# Today's Challenge: Find the First Repeated Character in a String
# Write a function that returns the first repeated character in a given string. If there’s no repeated character, return None.
# Example: first_repeated_char("hello") returns "l" and first_repeated_char("
# " returns None.
def first_repeated_char(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return char
        char_count[char] = True
        return None
    # The function iterates over each character in the string. If it encounters a character that is already
    # in the dictionary, it returns that character. If it doesn’t encounter any repeated characters,
    # it returns None.
    