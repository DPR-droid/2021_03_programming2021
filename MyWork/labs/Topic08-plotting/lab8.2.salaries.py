# lab8.2.salaries.py
# Messing with numpy
# Author David


import numpy as np
# it is a good idea to have your abosolute values set into 
# variables at the beginning of your program

minSalary = 20000
maxSalary = 80000
numberOfEntries = 10

# Modify the program so that the “random” salaries are the same each time the program is run, to make the program easier to test, 
# ie “seed” the random number generator. 
np.random.seed(1) 

salaries = np.random.randint(minSalary,maxSalary,numberOfEntries)

print(salaries)