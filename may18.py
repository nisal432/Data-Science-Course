#transpose = row column interchange
import numpy as np 
import pandas as pd
# npArr = np.arange(1,17).reshape(4,4)
# df = pd.DataFrame(npArr,columns=['Player', 'Enemy', 'Tree', 'sum'], index=['x-position', 'y-position', 'scale', 'distortion'])
# print(df.loc['x-position'])
# print(df)
# print(df.loc[['y-position', 'scale'], ['Enemy', 'Tree']])
# print(df.iloc[[1,2], [1,2]])

df = pd.read_csv('Salaries - Salaries.csv')
print(df.loc[df["TotalPay"] > 300000 , 'EmployeeName'] )
print(df.describe())

df.head().to_csv('topFive.csv')
df.describe().to_csv('described.csv')

