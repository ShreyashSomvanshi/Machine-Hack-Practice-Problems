'''
Find the largest element in a given array array1.

Example 1:
Input: array1 = [1,2,3,4]
Output: 4

Example 2:
Input: array1 = [10,40,33,4]
Output: 40
'''

# Solution:
def maximum_element(array):
  n = sorted(array1)
  return n[-1]
  
print(maximum_element(array1))
