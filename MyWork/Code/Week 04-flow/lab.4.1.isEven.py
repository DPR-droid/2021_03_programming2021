# lab.4.1.isEven.py
# Author David

# user inputs an integer
# using an if/else statement 
# The program will tell the user if the number is even or odd


number = int(input("enter an interger:"))


if (number % 2) == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")