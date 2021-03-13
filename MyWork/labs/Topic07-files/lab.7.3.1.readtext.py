# lab.7.3.1.readtext.py
# Author David

writeNumber(0)

import os.path
filename = "count1.txt"
if not os.path.isfile(filename):
    print("File does not exist")
    # initialise file here
    writeNumber(0)
