# lab11.9.readlog.py
# Author David

import pandas as pd

path = './data/'
logFilename = path + 'access.log'

colnames= ('ip',
    'dash1', 
    'userId', 
    'time', 
    'url', 
    'status code', 
    'size of response', 
    'referer', 
    'user agent', 
    'dunno'
)
df = pd.read_csv(logFilename, sep=' ', header= None, names=colnames)

print(df)
