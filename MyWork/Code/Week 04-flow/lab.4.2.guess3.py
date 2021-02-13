# lab.4.2.guess3.py
# Author David

# Guess the number game
# The program takes a number range 
# Then selects a random number between the range 
# Then keeps prompting the user until the correct number is selected


import random 

# Select range
x = 1
y = 10

# selects a random number from range
numberToGuess = random.randint(x,y)
# Testing to check the random number
# print(numberToGuess)

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: 
        print("too high")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was", numberToGuess)

