# importing necessary libraries

import pandas as pd
import datetime
from string import ascii_lowercase

# creating the lists

MyRow = []
for i in range(1, 21):
    MyRow.append(i)

MyString = []
for i in range(1, 21):
    MyString.append("".join(ascii_lowercase[:i]))

MyDate = []
start = datetime.date(2022,1,1)
while start <= datetime.date(2022,1,20):
    MyDate.append(datetime.datetime.strftime(start,'%Y-%m-%d'))
    start += datetime.timedelta(days=1)

# dictionary of lists
dict = {'MyRow': MyRow, 'MyString': MyString, 'MyDate': MyDate}

df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('File.csv', header=True, index=False)

# added
output = pd.read_csv('File.csv')
print(output)
