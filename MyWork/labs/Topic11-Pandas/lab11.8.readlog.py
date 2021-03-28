# lab11.7.readlog.py
# Author David

import pandas as pd

path = './data/'
logFilename = path + 'access.log'

df = pd.read_csv(logFilename, sep=' ', header=None)

print(df)
print(df.iloc[0])