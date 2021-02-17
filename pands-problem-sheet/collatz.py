# collatz.py
# Author David

# user inputs an integer
# using an if/else statement 
# The program will tell the user if the number is even or odd



# First number then we check if it is 0 in the while loop
number = int(input("Please enter a positive integer:"))

# Test print
# print(number)  


# Create a list for the number
numbers = []
# users input of number is appended to the list
numbers.append(int(number))

# Sanity check
# Using an if statement 
# Checks to see if the user has input a positive number
# If this fails it outputs a message
if number <= 0:
    print("No negativity or zeros allowed here")
else:
    # A while loop checks to see the value of number is equal to 1
    while number != 1:
        # Checks to see if the number is even
        if (number % 2) == 0:
            # Divides the number by two
            number = number // 2
        else:
            # If the number is odd it is multiplied by three and add one
            number = ((number * 3) + 1)
        # adds the output of the while loop to the list numbers    
        numbers.append(int(number))    
        # Test print
        # print(number)  

# Prints numbers list with spaces separating   
# Citation https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
print(*numbers, sep=' ')

    