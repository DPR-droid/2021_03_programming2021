# Author David
# lab3.3.normalise.py
# This program reads in a string and strips 
# any leading or trailing spaces.
# It also converts all the letters to lower case
# this program also outputs the lenght of the orginalstring
# and the normailsed one

rawString = input("Please enter a string:")
normailsedString = rawString.strip().lower()

lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normailsedString)

print("That String normailsed is :{}".format(normailsedString))
print("we reduced the input string from {} to {} characters".format(lenghtOfRawString,lenghtOfNormalised))
