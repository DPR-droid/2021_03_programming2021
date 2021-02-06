# lab2.3.randomGenerator.py
# Author David
# program that prints out a random number between 1 and 10


# import Module 
import random 

# Modified code to take user inputs
# Request user to input number range
print("Please input your range")
x = int(input("Enter lowest number: "))
y = int(input("Enter highest number: "))

number = random.randint(x,y)


# number = random.randint(1,10)
print("here is a random number {}".format(number))