'''
Consider an unsorted list as list1 containing multiple duplicate elements such as [a, b, c, a, d, e], provided all the elements are integers.
Remove all the duplicate elements from the given list and print the second largest number from the list.

Example 1: 
Input:  list1 = [1,2,3,4,5,6,7,8,9,10,2,1]
Output: 9
 

Example 2: 
Input: list1 = [1,2,3,3,4,1,7,8,3]
Output: 7

'''

# Solution:

def removingDuplicate(list1):
  list2 = sorted(list1)
  n =len(list2)
  return list2[n-2]
 
print(removingDuplicate(list1))


# My approach:
'''
list1 = [1,2,3,4,5,6,7,8,9,10,2,1]
listtt = set(list1)
list2 = list(listtt)
print(list2[-2])
'''
