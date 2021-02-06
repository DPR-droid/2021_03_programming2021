# Author David
# secondstring.py
# The program that takes asks a user to input a string and 
# outputs every second letter in reverse order


# Test Sentence
# sentence = "The quick brown fox jumps over the lazy dog."
# Test 1 reverse the sentence
# sentence = "The quick brown fox jumps over the lazy dog."[::-1]
# Test 2 reverse and select every second character
# sentence = ("The quick brown fox jumps over the lazy dog."[::-1])[::2]

# User input sentence
sentence = ((input("Please enter a sentence:")[::-1])[::2])

print(sentence)
