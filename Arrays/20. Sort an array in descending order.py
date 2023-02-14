'''
Print a given array array1 in the descending order of its elements. 

Example 1: 
Input: array1 = [2,3,1]
Output: [3, 2, 1]

Example 2: 
Input:  array1 = [98,99,97,96]
Output: [99, 98, 97, 96]
'''

# Solution:
def descending_order(array):
  i = sorted(array, reverse=True)
  return i
  
print(descending_order(array1))
