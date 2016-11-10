>>>x=[1,2,5,7,3,11,14,25]
>>>import numpy as np
>>>np_arr=np.array(x)
>>>np_arr

>>>arr=[[1,2],[13,4],[33,78]]
>>>np_2darr= np.array(arr)
>>>type(np_2darr)
numpy.ndarray

# indexing 
>>>np_2darr.tolist()
[[1, 2], [13, 4], [33, 78]]
>>>np_2darr[:]
array([[1, 2], [13,  4], [33, 78]])
>>>np_2darr[:2]
array([[1, 2], [13, 4]])
>>>np_2darr[:1]
array([[1, 2]])
>>>np_2darr[2]
array([33, 78])
>>>    np_2darr[2][0]
>>>33
>>>    np_2darr[:-1]
array([[1, 2], [13, 4]])

# basic operations
>>>>import numpy as np
>>>>np.arange(0.0, 1.0, 0.1)

>>>np.ones([2, 4])
>>>np.zeros([3,4])

>>>np.linspace(0, 2, 10)
>>>np.logspace(0,1)

>>>A=np.array([[0, 0, 0], [0, 1, 2], [0, 2, 4], [0, 3, 6]])
>>>B = np.array([n for n in range n for n in range(4)])
>>>less_than_3 = B<3 # we are filtering the items that are less than 3.
>>>B[less_than_3]
>>>np.diag(A)


# complex matrix operations 

>>>A = np.array([[1,2],[3,4]])
>>>A * A

>>>np.dot(A, A)
>>>A - A
>>>A + A
>>>np.transpose(A)
>>>A.T

>>>M = np.matrix(A)
>>> np.conjugate(M)
>>> np.invert(M)

>>>N = np.random.randn(1,10)
>>>N.mean()
>>>N.std()

#Reshaping 

>>>>A.reshape((1, r * c))
>>>A.flatten()
>>>np.repeat(A, 2)
>>>np.tile(A, 4)
>>>np.concatenate((A, B), axis=0)
>>>np.vstack((A, B))
>>>np.concatenate((A, B.T), axis=1)


#Random numbers

>>>from numpy import random
>>>#uniform random number from [0,1]
>>>random.rand(2, 5)
>>>>random.randn(2, 5)
