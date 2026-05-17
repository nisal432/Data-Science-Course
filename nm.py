import numpy as np
import pandas as pd
print(np.__name__)
nparr = np.array([2,3,4,2])
print(nparr)
print(nparr.dtype)

matrix1 = [[1,2,3,], [4,5,6], [7,8,9]]
print(matrix1)
print(type(matrix1))
b = np.matrix(matrix1)
print(b)
print(type(b))
print(b.ndim)
print(np.zeros(3, dtype= 'int'))
print(np.zeros((3, 3)))
print(np.ones(3, dtype= 'int'))
print(np.ones((3, 3)))
nparr2 = np.array([1,2,3,4])
print(nparr2*2)
c = np.arange(1, 37, 4)
print(c)
print(c.reshape(3,3))


d = np.array([1,2,3,4])
copy = d.copy()
copy += [4]
print(copy)
print(d)
randomArr = np.random.randint(0,40,10)
print(randomArr)
print(randomArr[0:-1])
for i in range(3):
	print(randomArr[i])
print(randomArr[:])


#first three element
print(randomArr[:3])

randomArr[:3] = 0
print(randomArr)

#index of the largest value in array
print(randomArr.argmax())

npArr3 = np.array([[1,2,3], [2,3,4], [4,7,8]])
npArr4 = np.array([[1,2,3], [2,3,4], [5,6,7]])
print(npArr4*npArr3)#element wise multiplication

print(npArr4@npArr3)#matrix multiplication 

labels = ["hello", "gg", "winner"]
print(pd.Series(labels))
