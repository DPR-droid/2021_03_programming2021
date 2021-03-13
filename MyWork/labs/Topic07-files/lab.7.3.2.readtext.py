# lab.7.3.2.readtext.py
# Author David

def readNumber():
    try:
        with open(filename) as f:
            number = int(f.read())
            return number
        except IOError:
            # this file will be created when we write back.
            # no file assumes first  time running
            # ie 0 previous runs
            return 0