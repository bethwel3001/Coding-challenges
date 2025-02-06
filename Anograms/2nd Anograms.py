# Why is this better?
# ✅ Less Code: Counter(word1) == Counter(word2) does all the frequency checking in one line.
# ✅ More Readable: No need for manual dictionary operations.
# ✅ Same Time Complexity: Both versions run in O(n) time.


from collections import Counter

def check_anagram(word1, word2):
    # Remove spaces and convert to lowercase    
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    return Counter(word1) == Counter(word2)  # Compare character frequencies directly

# Ask the user for two words
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Check if the words are anagrams
print(check_anagram(word1, word2))  # Output: True or False
