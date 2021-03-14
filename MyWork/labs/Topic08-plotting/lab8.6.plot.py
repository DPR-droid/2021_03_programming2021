# lab8.6.plot.py
# Author David


import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

# Modify the program so that the “random” salaries are the same each time the program is run, to make the program easier to test, 
# ie “seed” the random number generator. 
np.random.seed(1) 
salaries = np.random.randint(minSalary,maxSalary,numberOfEntries)


plt.hist(salaries)
plt.show()