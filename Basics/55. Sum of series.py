'''
Find the sum of a series as 1²+2²+3²+….+N² where the value of N would be given.

Example 1:
Input: N = 5
Output: 55

Example 2:
Input: N = 10
Output: 385
'''

# Solution:
def sumOfSeries(N):
  sum = 0
  for i in range(1,N+1):
    j = i*i
    sum += j
  return sum
  
print(sumOfSeries(N))

