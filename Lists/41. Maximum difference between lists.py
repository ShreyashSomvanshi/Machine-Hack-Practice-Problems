'''
Consider two lists as list1 and list2 containing the integer elements as [ a1, a2, a3, a4 ] and [ b1, b2, b3, b4 ].
Find the maximum difference between the same index elements.

Example 1:
Input:
list1 = [1,2,3]
list2 = [5,5,5]
Output: 4

Example 2:
Input:
list1 = [1,2,3]
list2 = [10,10,10]
Output: 9

Hints:
Use max() to compute the maximum
Use abs() to compute the difference

'''

# Solution:

def MaxDifference(list1,list2):
  l=[]
  for i in range(len(list1)):
    i_diff = list1[i] - list2[i]
    l.append(abs(i_diff))
      
  return max(l)
  
print(MaxDifference(list1,list2))
        

