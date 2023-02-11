'''
Consider a list as list1 consisting of some integer elements.
First, delete an element from the K-th position of the list, and then print the list excluding the first and last elements.

Ex. 1:
Input:  list1 = [1,2,3,4,5] K = 2
Output: [2, 4]

Ex. 2:
Input: list1 = [1,2,3,4,5,6,7,8] K = 4
Output: [2, 3, 4, 6, 7]
'''

# Solution:
def delete_access(list1,K):
  list1.pop(K)
  return list1[1:len(list1)-1]
  
print(delete_access(list1,K))





# My Try
'''
list1 = [1,2,3,4,5]
# print(list1[1:len(list1)-1])
def delete_access(list1,K):
  list1.pop(K)
  return list1[1:len(list1)-1]
  
# delete_access(list1,K)
print(delete_access(list1,2))
'''
