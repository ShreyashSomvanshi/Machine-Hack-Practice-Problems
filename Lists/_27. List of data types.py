'''
Show the data types of all the list items in the form of another list.

Example 1: 
Input:  list1 = [111,"aim",17.28]
Output: [<class 'int'>, <class 'str'>, <class 'float'>]
 
Example 2: 
Input: list1 = [99,87.3,"993.3",True]
Output: [<class 'int'>, <class 'float'>, <class 'str'>, <class 'bool'>] 
'''

# Solution
def dataType(list1):
  l=[]
  for i in range(len(list1)):
      a = type(list1[i])
      l.append(a)
  return l
  
print(dataType(list1))

# My approach:
'''
list1 = [111,"aim",17.28]
l=[]
# Output: 
for i in range(len(list1)):
    a = type(list1[i])
    l.append(a)
print(l)
'''
