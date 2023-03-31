import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])  
print(arr)  
print(type(arr)) 
print()
print("Number of elements in array :", np.size(arr))
print("Dimensions of array are :", np.shape(arr))

print()


## numpy (type,shape,dtype)
import numpy as np
import pandas as pd
a=np.array([[1,2,5],[3,4,7],[3,8,9]])
print(a)
print(type(a))
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)
b=np.array([["a"],["r"]])
print(b)
print(b.dtype)