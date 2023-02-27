'''
Consider two sets as set1 = {1, 2, 3, 4, 5} and set2 = {4, 5, 6, 7, 8}. Update the second set with elements that do not exist in the first set.
Finally, print the updated set.

Example 1:
Input:
set1 = {1, 2, 3, 4, 5, 6}
set2 = {3, 9, 4, 8, 7, 6}
Output: {7, 8, 9}


Example 2:
Input:
set1 = {11, 81, 31, 41, 15, 16}
set2 = {31, 19, 41, 81, 17, 61}
Output: {17, 19, 61}

'''

# Solution:

def unique_elements(set1,set2):
  v=set1.intersection(set2)
  s = set2-v
  d=set(sorted(s))
  print(d)
  
unique_elements(set1,set2)

