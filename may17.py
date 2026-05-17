import numpy as np 
# npArr = np.arange(0, 5)
# print(npArr/npArr)

#2d array multiplication 
# npArr2d = np.arange(1,9).reshape(2,4)
# print(npArr2d)
# nparr3 = np.arange(1,9).reshape(4,2)
# print(nparr3@npArr2d)

import pandas as pd
# labels = ["anish", "nama"]
# labels2 = ["anish", "naman"]
# myList = [1,4]
# myList2 = [1,5]
# print(pd.Series(labels))


# familiarity_with_python = {'anish':1, 'naman':2}
# print(pd.Series(data = labels, index= myList))
# print(pd.Series(data = labels2, index= myList2))
# check = pd.Series(data = labels, index= myList)
# check2 = pd.Series(data = labels2, index= myList2)


# print(pd.Series(familiarity_with_python))
# print(check+check2)
# print(check)
# print(check2)

data = {
    "name": ["Ram", "Sita"],
    "age": [25,1],
    "city": ["Kathmandu", "Lalitpur"]
}

df = pd.DataFrame(data)
print(df)
print(df[df["age"] > 20])
df['nameAddress']  =df['name'] + df['city']
print(df)
print(df['age']>20)
print(df[df['nameAddress']])
# to check = df.drop, df.drop implicit something, df.loc
