# Write a function that takes a sentence as input and returns the longest word in it.
# should ask the user for input

# the function
def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest
# the main program
def main():
    sentence = input("Please enter a sentence: ")
    print("The longest word is: ", longest_word(sentence))
main()
    