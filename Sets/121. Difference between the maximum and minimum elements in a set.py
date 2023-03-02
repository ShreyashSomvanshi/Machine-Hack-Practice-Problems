'''
Consider a set as set1 made of {a1,a2,a3,a4,a5,a6} provided a is an integer. First find the maximum 
element and minimum element of the given set and print the difference between the maximum and minimum element.

Example 1:
Input: set1 = {1,2,3,4,5,6}
Output: 5

Example 2:
Input: set1 = {11,22,32,41,51,61}
Output: 50
'''

# Solution:

def difference_max_min(set1):
  mini = min(set1)
  maxi = max(set1)
  diff = maxi-mini
  return diff
  
print(difference_max_min(set1))
