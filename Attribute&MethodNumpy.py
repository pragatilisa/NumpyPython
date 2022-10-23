Attributes of Numpy Includes the properties

import  numpy as np
x_1d=np.array([1,3,2])
y_1d=np.array([3,2,4])
z_2d=np.array([x_1d,y_1d])
print((x_1d))
#shape-to check the overall dimension
#print(x_1d.shape)
print(np.array([[1,3,2],[4,5,3]]).shape)
print(z_2d.shape)
#reshape to change the shape
print(z_2d.reshape((3,2))) # no of elements must be same i.e row*column must be same.
# dimension ndim()
print(z_2d.ndim) #its a 2d array

#item size -size of each elements of array in bytes
print(z_2d.itemsize)
k=np.array([1,3,4,2])
print(k.itemsize)
