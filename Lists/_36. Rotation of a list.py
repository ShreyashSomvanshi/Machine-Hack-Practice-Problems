'''
Consider a list as list1 consisting of the integer elements. Perform the 
left rotation of the list by the N-th position and show the resulting list.

Example 1:
Input:
list1 = [1,2,3,4]
N = 2
Output: [3, 4, 1, 2]

Example 2:
Input:
list1 = [10,20,30,40,50]
N = 3
Output: [40, 50, 10, 20, 30]
'''

# Solution:
def left_rotation(list1,N):
  return list1[N:]+list1[:N]

print(left_rotation(list1,N))


