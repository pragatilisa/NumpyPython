





# NumpyLibrary in Python Programming
Introduction & Operation using Numpy Library in python 

NumPy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python. It is open-source software. It contains various features including these important ones:

A powerful N-dimensional array object
Sophisticated (broadcasting) functions
Tools for integrating C/C++ and Fortran code
Useful linear algebra, Fourier transform, and random number capabilities

NumPy’s main object is the homogeneous multidimensional array.

It is a table of elements (usually numbers), all of the same type, indexed by a tuple of positive integers.
In NumPy dimensions are called axes. The number of axes is rank.
NumPy’s array class is called ndarray. It is also known by the alias array.

Numpy helps to do computational & statistical tasks.
Operations along with explaination are mentioned on these respository.
Array Types-
1.Vector-Array With 1 Dimension (simple terms-its a linear list)

      x=np.array([1,3,4,2]
      >>x
      >>[1,3,4,2]
 
2.Matrix- Array with 2D (Its is like a mathematical matrix which are basically lists of list)

       y=np.array([[1,3,2],[3,5,3]]) 
       >>y
       >>[[1,3,2],[3,5,3]]
       
3.Tensor- Array with 3D or more (Easy way to spot is use 'ndim' function or spot the no. of square brackets)

      a_2d=np.array([[1,3,2],[1,5,3]])
      b_2d=np.array([[2,4,2],[8,5,4]])
      c_3d=np.array([a_2d,b_2d])
      >>print(c_3d)
      >>[[[1 3 2]
        [1 5 3]]
         [[2 4 2]
         [8 5 4]]]
         
         
   Attributes of a NumPy Array
   
   NumPy array (ndarray class) is the most used construct of NumPy in Machine Learning and Deep Learning. Let us look into some important attributes of this NumPy     array.

Let us create a Numpy array first, say, array_A.

Pass the above list to array() function of NumPy

            array_A = np.array([ [3,4,6], [0,8,1] ])
Now, let us understand some important attributes of ndarray object using the above-created array array_A.

(1) ndarray.ndim

ndim represents the number of dimensions (axes) of the ndarray.

e.g. for this 2-dimensional

            array_A = np.array [ [3,4,6], [0,8,1]] 
        
            value of ndim will be 2. This ndarray has two dimensions (axes) - rows (axis=0) and columns (axis=1)

(2) ndarray.shape

shape is a tuple of integers representing the size of the ndarray in each dimension.

e.g. for this 2-dimensional 
            
            array_A=array [ [3,4,6], [0,8,1]], value of shape will be (2,3) 
            because this ndarray has two dimensions - rows and columns - and the number of rows is 2 and the number of columns is 3

(3) ndarray.size

size is the total number of elements in the ndarray. It is equal to the product of elements of the shape. e.g. for this 2-dimensional 
            
            array_A= np.array [ [3,4,6], [0,8,1]]
            shape is (2,3), size will be product (multiplication) of 2 and 3 i.e. (2*3) = 6. Hence, the size is 6.

(4) ndarray.dtype

dtype tells the data type of the elements of a NumPy array. In NumPy array, all the elements have the same data type.

e.g. for this NumPy 
            
            array_A=array [ [3,4,6], [0,8,1]] dtype will be int64

(5) ndarray.itemsize

itemsize returns the size (in bytes) of each element of a NumPy array.

e.g. for this NumPy 
            
            array_A=array [ [3,4,6], [0,8,1]]
            itemsize will be 8, because this array consists of integers and size of integer (in bytes) is 8 bytes.
   
   Numpy Methods
   
   Numpy methods refers to the operations that can be done on array.
   
   Let us create a Numpy array first, say, array_A.

Pass the above list to array() function of NumPy

            array_A = np.array([ [3,4,6], [0,8,1] ])
            
 (1).Flatten() 
 
 It returns an array collapsed into 1D.
 flatten()- inside the barckets we can specify row,colums or both to flatten.To flatten rows pass 'C' gor colums pass 'F' or (C,F)
           
           array_A=np.array([ [3,4,6], [0,8,1] ])
           >>array_A.flatten()
           >> [3,4,6,0,8,1]
           s=np.array([[4,5,9,5],[2,7,8,5]]) 
           print(s.flatten('F')) # ‘F’ means to flatten in column-major (Fortran- style) order
           print(s.flatten('C')) # ‘C’ means to flatten in row-major (C-style) order
           >> [4 2 5 7 9 8 5 5]
           >> [4 5 9 5 2 7 8 5]
           
 (2). Reshaping()
  
  It reshape the array dimension based on the inputted dimension.The reshape array must have same dimension as the original array
  
           array_A=np.array([ [3,4,6], [0,8,1] ])
           >> array.reshape(3,2)
           >> [ [3,0],
                [4,8],
                [6,1] ]
   
   
