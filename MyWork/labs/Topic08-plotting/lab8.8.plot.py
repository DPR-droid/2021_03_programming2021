# lab8.8.plot.py
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
ages = np.random.randint(low=21, high=65, size=numberOfEntries)


plt.scatter(ages, salaries)
# plt.show()

# add x squared
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints # multiply each entry by itself

plt.plot(xpoints, ypoints, color='r')
plt.show()