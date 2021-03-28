# lab11.11.readlog.py
# Author David

import pandas as pd
import re

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

# drop a column
df.drop(columns=['dash1', 'userId'], inplace=True)


# remove the  [] from time
df['time'] = df['time'].apply(lambda x: re.search('[\w:/]+', x).group())
# for the task you may want to use a normal function instead of lambda
'''
def getNewValue(x):
    newvalue = re.search('[\w:/]+', x).group()
    # do your stuff
    return newvalue

df['time'] = df['time'].apply(getNewValue)
'''