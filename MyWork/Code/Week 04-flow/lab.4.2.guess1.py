# lab.4.2.guess1.py
# Author David

# Guess the number game
# The user guesses a number
# The program should keeps prompting the user until the correct number

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print("Wrong")
    guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)