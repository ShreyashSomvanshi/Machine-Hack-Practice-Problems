'''
Find the sum of the square and the square roots of the given integer N.

Example 1: 
Input: N = 4
Output: 18.0

Example 2: 
Input: N = 17
Output: 293.12310562561765
'''

# My Solution:

import math
def sumOfSqSqroot(N):
  sqr = N*N
  sqt = math.sqrt(N)
  return sqr+sqt
  
print(sumOfSqSqroot(N))
