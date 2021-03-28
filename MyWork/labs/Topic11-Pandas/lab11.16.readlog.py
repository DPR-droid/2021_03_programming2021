# lab11.15.readlog.py
# Author David

import pandas as pd
import re
import matplotlib.pyplot as plt


def clearSqrBrackets(string):
    return 

path = './data/'
logFilename = path + 'access.log'

colNames= ('ip',
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
df = pd.read_csv(logFilename, sep=' ', header= None, names=colNames)

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

# Normal date and time
df['time'] = pd.to_datetime(df['time'], format='%d/%b/%Y:%H:%M:%S')
print (df.dtypes)
# output row of id 0
print(df.iloc[0])

start_date = pd.to_datetime('2021/02/15 23:00')
end_date = pd.to_datetime('2021/02/15 23:59:59')


#newdf = df.loc[(df['time'] > start_date) & (df['time'] < end_date)]
#newdf = df[df.time.between(start_date, end_date)]
df = df.set_index(['time'])
newdf = df['2021/02/15 23:00':'2021/02/15 23:59:59']
#newdf = df.between_time('23:00', '23:59') # this is times every day
print (newdf)


# Downloaded Sample size
downloadSamples = df['size of response'].resample(rule='30Min').mean()
print(downloadSamples)

# plot
downloadSamples.plot()
plt.show()
