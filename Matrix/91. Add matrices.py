'''
Consider two 3x3 matrices as A and B such as [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]] and 
[[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]] provided all the elements are integers. Write a python program 
to perform matrix addition of the given two matrices using a for-loop and print the resultant output matrix.

Example 1:
Input:
A = [[1,1,1],[1,1,1],[1,1,1]]
B = [[1,1,1],[1,1,1],[1,1,1]]
Output: [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

Example 2:
Input:
A = [[1,1,1],[1,1,1],[1,1,1]]
B = [[2,2,2],[2,2,2],[2,2,2]]
Output: [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
'''

# Solution: By Chat GPT
def matrix_additon(matrix1,matrix2):
  result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  for i in range(len(A)):
    for j in range(len(A[0])):
      result[i][j] = A[i][j] + B[i][j]

  return result
  
print(matrix_additon(A,B))




# My approach: Wrong
'''
# A = [[1,1,1],[1,1,1],[1,1,1]]
# B = [[1,1,1],[1,1,1],[1,1,1]]
A = [[1,1,1],[1,1,1],[1,1,1]]
B = [[2,2,2],[2,2,2],[2,2,2]]
# Output:

# [[3, 3, 3], [3, 3, 3], [3, 3, 3]]

h = []
import numpy as np
# Output:

for i in range(len(A)):
    g = np.asarray(A[i])
    for j in range(len(B)):
        u = np.asarray(B[j])
    f = g+u
    k = list(f)
    h.append(k)
print(h)
'''
