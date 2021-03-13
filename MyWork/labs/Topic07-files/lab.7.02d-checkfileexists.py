# lab.7.02d-checkfileexists.py
# Author David

import os.path
filename = "count1.txt"
if not os.path.isfile(filename):
    print("File does not exist")
    # initialise file here
