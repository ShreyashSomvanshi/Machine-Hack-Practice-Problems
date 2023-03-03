'''
Consider two arrays as array1 and array2 such as [a1, b1, c1 ] and [ a2, b2, c2 ] provided all 
the elements are integers. Now create a new sorted array merging all the elements of both the arrays 
and print the difference between the mean and median of the new array.

Example 1:
Input:
array1 = [10,5]
array2 = [9]
Output: 3.0

Example 2:
Input:
array1 = [10,1]
array2 = [9,16]
Output: 4.0
'''

# Solution:


# My Approach:

array1 = [10,1]
array2 = [9,16]
import numpy as np
import statistics
# Output:

# 4.0
r=array1+array2
concat = np.asarray(r)
l=sorted(concat)
r=statistics.mean(l)
u=statistics.median(l)
print(u)





