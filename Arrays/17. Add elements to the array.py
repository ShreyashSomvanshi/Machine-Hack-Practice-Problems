'''
Consider an array as array1 containing the integer elements. Add an element N to the K-th position of the array and show the updated array.

Example 1: 
Input: array1 = [1,2,4] ; K = 2 ; N = 3
Output: [1, 2, 3, 4]

Example 2: 
Input:  array1 = [89,91,92] ; K = 1 ; N = 90
Output: [89, 90, 91, 92]

'''

# My Solution:
def add_a_element(array,K,N):
  array.insert(K,N)
  return array
  
print(add_a_element(array1,K,N))

