# lab11.2.createdata.py
# Author David


import pandas as pd

listdata = [
    ['John', 'maths',       23],
    ['John', 'programming', 66],
    ['Mary', 'maths',       45],
    ['Mary', 'programming', 33],
    ['Mark', 'maths',       57],
    ['Mark', 'programming', 70],
    ['Pete', 'maths',       73],
    ['Pete', 'programming', 61]
]


df = pd.DataFrame(listdata, columns=['name','subject','grade'])
print(df.head(3))

print(df.describe())
print(type(df.describe()))
