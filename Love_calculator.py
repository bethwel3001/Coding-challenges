# 💡 "Love Calculator" Challenge
# Write a Python program that:

# Takes two names as input.
# Counts the occurrences of the letters in "TRUE LOVE" in both names.
# Combines the counts to form a "love percentage" (just for fun).
# Outputs the love percentage as a percentage value (e.g., 42%).
#
# 💡 Example Input/Output
#   
# :
# Input: "John" "Mary"
# Output: "Your love score is 72%."
#
# 💡 Example Input/Output
# Th function
def love_calculator(name1, name2):
    # Define the letters in "TRUE LOVE"
    love_letters = "TRUELOVE"
    # 
    # Initialize counters for each letter in "TRUE LOVE"
    love_count = {letter: 0 for letter in love_letters}
    # Count the occurrences of each letter in "TRUE LOVE" in both names
    for name in [name1, name2]:
        for letter in love_letters:
            love_count[letter] += name.lower().count(letter)
            # Combine the counts to form a "love percentage"
            love_percentage = sum(love_count.values()) / (len(love_letters) * 2
                                                          # Output the love percentage as a percentage value
                                                          return f"Your love score is {love_percentage:.0f}%."
                                                          # Test the function with example inputs
                                                          print(love_calculator("John", "Mary"))  # Output: "Your love score is
                                                          print(love_calculator("John", "Mary"))  # Output: "Your love score is
                                                          
