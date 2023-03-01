'''
Consider a list as list1 such as [ a1, a2, a3, a4, a5, a6 ] provided all the list elements are independent natural numbers. 
First, convert the given list into a NumPy array and reverse the NumPy array. Finally, print the reversed array.

Example 1:
Input: list1= [1, 2, 3, 4, 5, 6]
Output: [6 5 4 3 2 1]

Example 2:
Input: list1= [99,98,97,96,95,94]
Output: [94 95 96 97 98 99] 

'''

# Solution:
#Importing NumPy Library
import numpy as np
def revArray(l):
  d = np.asarray(l)
  return d[::-1]
  
print(revArray(list1))

