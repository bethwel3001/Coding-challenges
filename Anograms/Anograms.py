# Write a function that checks if two words are anagrams.
# **An anagram means two words contain the same letters, just rearranged.**
# should ask the user for an input the words
# should return True if the words are anagrams, False otherwise.
def check_anagram(word1, word2):
    # Remove spaces and convert to lowercase    
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    # Check if the lengths of the words are equal
    if len(word1) != len(word2):
        return False
    
    # Count the frequency of each letter in both words
    freq_dict = {}
    for char in word1:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    
    for char in word2:
        if char in freq_dict:
            freq_dict[char] -= 1
        else:
            return False
    
    # Check if all frequencies are zero
    for freq in freq_dict.values():
        if freq != 0:
            return False
    
    return True
# Ask the user for two words
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
# Check if the words are anagrams
print(check_anagram(word1, word2))  # Output: True or False
