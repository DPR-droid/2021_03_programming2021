# lab2.3.normalise.py
# Author David
# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letter to lower case
# This program also outputs the lenght of the orginal string
# and the normalised on.

rawString = input("Please enter a string:")
normalisedString = rawString.strip().lower()

lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

print("That String normalised is :{}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(lenghtOfRawString, lenghtOfNormalised))
