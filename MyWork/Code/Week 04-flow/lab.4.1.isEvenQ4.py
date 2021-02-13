# lab.4.1.isEven.py
# Author David

# user inputs an integer
# using an if/else statement 
# The program will tell the user if the number is even or odd



# first number then we check if it is 0 in the while loop
number = int(input("enter number (0 to quit): "))

while number != -1:
     

    if (number % 2) == 0:
        print(number, "is an even number")
    else:
        print(number, "is an odd number")

    # read the next number and check if 0
    number = int(input("enter another (0 to quit): "))