import numpy as np
#find index where 7 should be inserted 
arr=np.array([6,7,8,9])
x=np.searchsorted(arr,7)
print(x)

#indexes where the values 2,4 and 6 

arr=np.array([1,3,5,7])
x=np.searchsorted(arr,[2,4,6])
print(x)