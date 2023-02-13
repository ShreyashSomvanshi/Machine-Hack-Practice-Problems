'''
Consider two sets as set1 and set2 such as {x1, x2, x3, x4,x5, x6} provided x is an integer. Print all the identical elements from the two sets.

Example 1: 
Input: 
set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 9, 4, 8, 7, 6}
Output: {3, 4, 6}
 
Example 2: 
Input:  
set1 = {11, 12, 31, 41, 15, 16}
set2 = {31, 19, 41, 81, 17, 61}
Output: {31, 41}

'''

# Solution:
def identical_elements(set1,set2):
  x = set1.intersection(set2)
  return x
  
print(identical_elements(set1,set2))

# My approach
'''
set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 9, 4, 8, 7, 6}
x = set1.intersection(set2)
print(x)
'''
