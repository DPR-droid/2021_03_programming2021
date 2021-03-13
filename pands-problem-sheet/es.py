# es.py
# This program that reads in a text file and outputs the number of e's it contains
# The program should take the filename from an argument on the command line.
# Author David

# Moby Dick text 
# https://www.gutenberg.org/files/2701/old/moby10b.txt

# https://realpython.com/python-command-line-arguments/
import sys

# https://www.w3schools.com/python/python_regex.asp#findall
import re


filename = sys.argv[1]

# Set variables to zero
count = 0
totalCount = 0

with open(filename, "r") as f:
    for line in f:
        count = len(re.findall("e", line)) 
        # Adding all lowercase e's in string to total count
        totalCount = totalCount + count
        # Test to see totalcount 
        # print("in loop" + str(totalCount))

# Output 
print(totalCount)