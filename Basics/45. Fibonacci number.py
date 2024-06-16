'''
Check whether a given number N is a Fibonacci number or not.

Example 1:
Input: N = 6769
Output: False

Example 2:
Input: N = 4181
Output: True

Constraints: Print True if the given number is a Fibonacci number and print False if the number is not a Fibonacci number.
'''
# Soln:
def fibonacciNumber(N):
  a, b = 0, 1
  while a < N:
      a, b = b, a + b
  return a == N
  
print(fibonacciNumber(N))
