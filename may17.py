import numpy as np 
# npArr = np.arange(0, 5)
# print(npArr/npArr)

#2d array multiplication 
npArr2d = np.arange(1,9).reshape(2,4)
print(npArr2d)
nparr3 = np.arange(1,9).reshape(4,2)
print(nparr3@npArr2d)