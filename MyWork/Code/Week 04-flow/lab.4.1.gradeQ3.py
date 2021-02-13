# lab.4.1.gradeQ3.py
# Author David

# This program reads in 
# a students percentage
# and prints out the 
# corresponding grade

percentage = float(input("Enter the percentage: "))
# Rounding the percentage number 
roundedpercentage = round(percentage)
# print(roundedpercentage)

# be careful with ands and ors
if roundedpercentage < 0 or percentage > 100:
    # Later we will show you error handling 
    # This should really throw an error
    print("Please enter a number between 0 and 100")
elif roundedpercentage < 40: # we know it is greater than 0
    print("Fail")
elif roundedpercentage < 50: # between 40 and 49
    print("Pass")
elif roundedpercentage < 60: # between 50 and 59
    print("Merit 1")
elif roundedpercentage < 70: # between 60 and 69
    print("Merit 2")
else: # the only option left is between 70 and 100
    print("Distinction")
