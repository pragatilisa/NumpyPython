Attributes & Methods of Numpy Includes the properties

import  numpy as np
x_1d=np.array([1,3,2])
y_1d=np.array([3,2,4])
z_2d=np.array([x_1d,y_1d])
print((x_1d))
#shape-to check the overall dimension
print(x_1d.shape)
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
#converts array into 1D
print(z_2d.flatten())
#sizeofarray-the multiplication of rows & columns
print(z_2d.size)

s=np.array([[4,5,9,5],[2,7,8,5]]) 
       print(s.flatten('F')) # ‘F’ means to flatten in column-major (Fortran- style) order
       print(s.flatten('C')) # ‘C’ means to flatten in row-major (C-style) order
       >> [4 2 5 7 9 8 5 5]
       >> [4 5 9 5 2 7 8 5]

Output:
 [1 3 2]
(3,)
(2, 3)
(2, 3)
[[1 3]
 [2 3]
 [2 4]]
2
4
4
[1 3 2 3 2 4]
6
