#Creating 2D Array From 1D
import numpy as np

x_1d=np.array([1,3,2])
y_1d=np.array([3,2,4])
z_2d=np.array([x_1d,y_1d])
print((x_1d))
print(y_1d)
print(z_2d)

Output:
[1 3 2]
[3 2 4]
[[1 3 2]
 [3 2 4]]

#Creating 3D Array From 2D
import numpy as np
a_2d=np.array([[1,3,2],[1,5,3]])
b_2d=np.array([[2,4,2],[8,5,4]])
c_3d=np.array([a_2d,b_2d])
print(c_3d)

Output:
[[[1 3 2]
  [1 5 3]]

 [[2 4 2]
  [8 5 4]]]
