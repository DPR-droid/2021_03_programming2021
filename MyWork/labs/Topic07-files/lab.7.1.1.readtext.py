# lab.7.1.1.readtext.py
# Author David

# the with statement will automatically close the file
# when it is finished with it

with open("test-a.txt") as f:
    data = f.read()
    print(data)
