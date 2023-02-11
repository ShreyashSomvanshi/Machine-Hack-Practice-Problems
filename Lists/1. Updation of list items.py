'''
Add a given element N to the K-th position of the list list1.

Ex 1:
Input: list1 = [1,2,3] ; N = 8 ; K = 1
Output: [1, 8, 2, 3]
'''

# Solution:
def updation(list1,N,K):
  list1.insert(K,N)
  return list1
print(updation(list1,N,K))

# My try
'''

list1 = [1,2,3]
def updation(list1,N,K):
  list1.insert(K,N)
  return list1
print(updation(list1,8,1))

# N = 8
# K = 1

'''
