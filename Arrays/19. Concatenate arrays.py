'''
Consider two arrays as array1 and array2 consisting of the integer elements. 
Concatenate both the arrays and print the sum of the elements of the concatenated array.

Example 1: 
Input: 
array1 = [1, 1, 1]
array2 = [1, 1, 1]
Output: 6
 

Example 2: 
Input: 
array1 = [1, 2, 3]
array2 = [1, 2, 3]
Output: 12
'''

# Solution
def sum(array1,array2):
  a = 0
  b = 0
  for i in range(len(array1)):
    a = a+array1[i]
  
  for j in range(len(array2)):
    b = b+array2[j]
    
  c = a+b  
  return c
  
  
print(sum(array1,array2))


# My Approach:
'''
array1 = [1, 2, 3]
a = 0
for i in range(len(array1)):
    a = a+array1[i]
print(a)
'''  
  
