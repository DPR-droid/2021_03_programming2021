# Author David
# lab3.2.convert.py
# take an input of an amount in the form -9.44 (9 dollarsand 44 cent), 
# the issue there may or may not be a minus sign
# and the bank takes in the amountin cent, (944).
# The program takes in a float amount of dollars, 
# and returns that absolute amount in cent.


import math

# Request Users input
# Test input
# numberOffloat = -9.44
# User input
numberOffloat = float(input("Enter a float number:"))


# Takes users input multiplies by 100, then rounds the number,
# then creates an absolute number
# Test 1
# convertToCent = (numberOffloat*100)
# Test 2
# convertToCent = round(numberOffloat*100)
# Final version
convertToCent = abs(round(numberOffloat*100))
print('{} is {} cent'.format(numberOffloat,convertToCent))