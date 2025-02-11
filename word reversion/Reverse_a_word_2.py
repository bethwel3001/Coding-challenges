def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

# Test
sentence = input("Please enter a sentence: ")
print("The reversed sentence is:", reverse_words(sentence))
