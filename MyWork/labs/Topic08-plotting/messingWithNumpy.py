# Messing with numpy
# Author David

import numpy as np

listOfNumbers = [1,2,5,6]
numbers = np.array([1,2,3,4,5])

#listOfNumbers = listOfNumbers + 3
numbers = numbers * np.array([2,5,7,9,6])

print(listOfNumbers)
print (numbers)

randomNumbers = np.random.randint(100, 200, 5)
print(randomNumbers)

normalNumbers = np.random.normal(size = 100)
print(normalNumbers)