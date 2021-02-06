# lab3.2.absolute.py
# Author David

# Give the absolute value of a number
# In the question, number is ambigious but the 
# output implies that we should be dealing with floats
# So I am casting the inout to a float

number = float(input("Enter a number:"))
absoluteValue = abs(number)
print('The absolute value of {} is {}'.format(number,absoluteValue))
