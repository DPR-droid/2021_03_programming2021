# weekday.py
# Author David

# The program that outputs whether or not today is a weekday
# Citation https://www.w3schools.com/python/python_datetime.asp


# import datetime function 
import datetime

# Set x to the current dateand time
x = datetime.datetime.now()

# Test function to check numbered output for different days
# x = datetime.datetime(2021, 2, 13)
# x = datetime.datetime(2021, 2, 14)
# x = datetime.datetime(2021, 2, 15)
# x = datetime.datetime(2021, 2, 16)
# x = datetime.datetime(2021, 2, 17)
# x = datetime.datetime(2021, 2, 18)
# x = datetime.datetime(2021, 2, 19)

# Check output
# print(x.strftime("%w"))   
# print(x.strftime("%A")) 

# use strftime to output the weekday as a number and set to dayNumber
# %w Weekday as a number 0-6, 0 is Sunday
dayNumber = int((x.strftime("%w")))

# Test output of dayNumber
# print(dayNumber)

# Use if/elif/else to output answer for the user
if dayNumber == 0:
    print("It is the weekend, yay!")
elif dayNumber == 6:
    print("It is the weekend, yay!")
else:
    print("Yes, unfortunately today is a weekday.")
