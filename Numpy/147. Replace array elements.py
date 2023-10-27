'''
Consider a NumPy array as array1 containing three float elements such as [ a, b, c ]. Replace an 
array element with a value X if the array element is less than the particular constant limit Y. Assume 
the value of the constant Y as 44.404

Example 1:
Input:
array1= [112.343, 123.35,  22.34]
X = 99.01
Output: [112.343 123.35   99.01 ]

Example 2:
Input:
array1= [89.43, 33.34, 222.34]
X = 99.01
Output: [ 89.43  99.01 222.34]

'''

# Solution:

import numpy as np
Y = 44.44

def repl(array):
  for i in range(len(array)):
    if array[i] < Y:
      array[i] = X
  return np.array(array)
  
print(repl(array1))



