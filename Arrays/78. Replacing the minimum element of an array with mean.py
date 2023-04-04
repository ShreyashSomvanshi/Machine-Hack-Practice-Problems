'''
Consider an unsorted array as array1 such as [ a1, b1, c1 ] provided all the elements are integers. 
Write a python program to convert the unsorted array into a sorted array and replace the minimum 
elements of the array with the mean of the array. Finally print the resultant array.

Example 1:
Input: array1 = [1,5,4,2,3]
Output: [3.0, 2, 3, 4, 5]

Example 2:
Input: array1 = [10,7,12,11,3]
Output: [8.6, 7, 10, 11, 12]

'''

# Solution:

def sorting_and_replacing(array1):
  array1 = sorted(array1)

  i = 0
  for j in array1:
    i = i+j
  avg = i/len(array1)
  array1[0] = avg
  return array1

print(sorting_and_replacing(array1))


