'''
Consider an unsorted array as array1 such as [ a1, b1, c1 ]. Move all the zeros in 
the array to the end of the array and show the resulting array.

Example 1:
Input: array1 = [1,0,1,0,1,0,1,0]
Output: [1, 1, 1, 1, 0, 0, 0, 0]

Example 2:
Input: array1 = [7,0,0,3,4,0,6,5]
Output: [7, 3, 4, 6, 5, 0, 0, 0]
'''

# Solution:
def move_zeros_to_end(array):
  l=[]
  for i in range(len(array)):
    if array[i] != 0:
      l.append(array[i])
    
  diff = len(array)-len(l)
  for i in range(diff):
    l.append(0)
  return l

print(move_zeros_to_end(array1))

# My Approach:
'''
def move_zeros_to_end(array):
    
    l=[]
    for i in range(len(array)):
        if array[i] != 0:
            l.append(array[i])
        
    diff = len(array)-len(l)
    for i in range(diff):
        l.append(0)
    return l
array1 = [7,0,0,3,4,0,6,5]
# # # Output:

# # # [7, 3, 4, 6, 5, 0, 0, 0]
  
print(move_zeros_to_end(array1))
'''


