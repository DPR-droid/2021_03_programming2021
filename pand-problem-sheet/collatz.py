# lab.4.1.isEven.py
# Author David

# user inputs an integer
# using an if/else statement 
# The program will tell the user if the number is even or odd



# first number then we check if it is 0 in the while loop
number = int(input("Please enter a positive integer:"))

print(number)

if number <= 0:
    print("No negativity or zeros allowed here")
else:
    while number != 1:
        if (number % 2) == 0:
            number = number // 2
        else:
            number = ((number * 3) + 1)
        
        print(number)

    