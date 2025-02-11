# Write a function that takes a sentence and returns it with each word reversed, but the word order stays the same.
# should take an input from the user
def reverse_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Initialize an empty list to store the reversed words
    reversed_words = []
    
    # Iterate over each word in the list
    for word in words:
        # Reverse the word using slicing
        reversed_word = word[::-1]
        
        # Append the reversed word to the list
        reversed_words.append(reversed_word)
    
    # Join the reversed words back into a sentence with spaces between them
    reversed_sentence = ' '.join(reversed_words)
    
    # Return the reversed sentence
    return reversed_sentence
# Test the function with a user input
sentence = input("Please enter a sentence: ")

reversed_sentence = reverse_words(sentence)
print("The reversed sentence is: ", reversed_sentence)  
