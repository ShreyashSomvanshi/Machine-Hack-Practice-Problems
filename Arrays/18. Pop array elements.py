'''
Consider an array as array1 containing some integer elements. Delete an element from the K-th position of the array and show the updated array.

Example 1: 
Input: array1 = [1,2,3] ; K = 0
Output: [2, 3]
 
Example 2: 
Input:  array1 = [90,20,30,11] ; K = 2
Output: [90, 20, 11]
'''

# Solution:
def delete_an_element(array,K):
  array.pop(K)
  return array
  
print(delete_an_element(array1,K))

## OR

def delete_an_element(array,K):
  for i in range(len(array)):
    if i == K:
        del(array[i])
  return array
  
print(delete_an_element(array1,K))


# My Approaches:
'''
def delete_an_element(array,K):
  array.pop(K)
  return array
  
print(delete_an_element(array1,K))
'''
# And
'''
for i in range(len(a)):
    if i == k:
        del(a[i])
print(a)
'''
