'''
Consider two 3x3 matrices as A and B such as [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]] 
and [[x1, y1, z1], [x2, y2, z2],[x3, y3, z3]] provided all the elements are integers. 
Perform matrix multiplication of the given two matrices using a for-loop and print the resultant output matrix.

Example 1:
Input:
A = [[1,1,1],[1,1,1],[1,1,1]]
B = [[1,1,1],[1,1,1],[1,1,1]]
Output: [[3, 3, 3], [3, 3, 3], [3, 3, 3]]

Example 2:
Input:
A = [[1,1,1],[1,1,1],[1,1,1]]
B = [[1,2,3],[4,5,5],[6,7,8]]
Output: [[11, 14, 16], [11, 14, 16], [11, 14, 16]]

'''

# Solution :

def matrix_multiplication(matrix1,matrix2):
  result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate through each row of the first matrix
  for i in range(len(A)):
    # iterate through each column of the second matrix
    for j in range(len(B[0])):
        # iterate through each element of the first row and the second column
      for k in range(len(B)):
          result[i][j] += A[i][k] * B[k][j]
  print(result)
  
matrix_multiplication(A,B)
