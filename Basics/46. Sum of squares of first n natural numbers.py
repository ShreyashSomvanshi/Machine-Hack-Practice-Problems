'''
Find the sum of squares of the first N natural numbers.

Example 1:
Input: N = 2
Output: 5

Example 2:
Input: N = 5
Output: 55
'''

# Soln:

def sumOfSquares(N):
  sum = 0
  for i in range(1, N+1):
    sum += i ** 2
  return sum
  
print(sumOfSquares(N))
