'''
Consider two lists as list1 and list2 such as [a1, b1, c1] and [a2, b2, c2] provided a, b, and c are strings. 
Add lists list1 and list2 and sort the resultant list in alphabetical order. Finally, show the sorted list.

Example 1: 
Input:  
list1 = ["A", "E", "C"]
list2 = ["G", "F", "B"]

Output: 
['A', 'B', 'C', 'E', 'F', 'G']


Example 2: 
Input: 
list1 = ["bac", "man", "che"]
list2 = ["dot", "rma", "juv"]

Output: 
['bac', 'che', 'dot', 'juv', 'man', 'rma']

'''

# Solution:

#Write the code 
def addition(list1,list2):
  listt = list1+list2
  listt.sort()
  return listt
  
print(addition(list1, list2))





# My approach:

def addition(list1,list2):
  listt = list1+list2
  listt.sort()
  return listt
  
list1 = ["A", "E", "C"]
list2 = ["G", "F", "B"]

print(addition(list1, list2))
