# lab9.2.myFunctions.py
# Author David

import numpy as np
import matplotlib.pyplot as plt

# make the array of occurences
possibleCounties = ['Gaillimh', 'Baile Átha Cliath', 'Mhaigh Eo',' Thiobraid Árann', 'Loch Garman']
# pick 100 randonly from possible counties with the frequece set in p
counties = np.random.choice(
    possibleCounties, 
    p=[0.1, 0.3, 0.2, 0.12, 0.28],
    size=(100)
)

# right now we need the number of occurances of each county
# this returns a tuple of the unique values and how many time they appear
unique, counts = np.unique(counties, return_counts=True)
# we can now put this into a pie plot
plt.bar(unique, counts)

plt.show()