'''
Consider two rectangular matrices as matrix1 and matrix2 such as [[a1,a2], [a3,a4],[a5,a6]] 
and [[b1,b2,b3],[b4,b5,b6]] provided a and b are integers. Write a python code to perform 
multiplication of the given two matrices and print the resulting output.

Example 1:
Input:
matrix1 = [[1, 2],
          [2, 3],
          [4,5]]
matrix2 = [[7, 5, 4],
          [6, 7, 5]]
Output:
[[19 19 14]
 [32 31 23]
 [58 55 41]]

Example 2:
Input:
matrix1 = [[3,3],
          [4,4],
          [5,5]]
matrix2 = [[3,3,3],
          [5,5,5]]
Output:
[[24 24 24]
 [32 32 32]
 [40 40 40]]

Hints: Use np.matmul() or np.dot() to perform multiplication
'''

# Soln:
# importing Numpy package
import numpy as np
print(np.matmul(matrix1, matrix2))



