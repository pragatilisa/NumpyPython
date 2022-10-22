# Numpy Python
Introduction & Operation in Numpy in Python

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
