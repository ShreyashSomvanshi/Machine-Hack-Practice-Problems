'''
Show all the divisors of the given integer N in the form of a list.

Example 1:
Input: N = 8
Output: [1, 2, 4, 8]

Example 2:
Input: N = 9
Output: [1, 3, 9]

'''

# Soln:
def divisors(N):
  r = []
  for i in range(1, N+1):
    if N%i == 0:
      r.append(i)
  return r
      
print(divisors(N))
