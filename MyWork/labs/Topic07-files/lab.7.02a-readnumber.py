# lab.7.02a-readnumber.py
# Author David


filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number

# test it
num = readNumber()
print(num)