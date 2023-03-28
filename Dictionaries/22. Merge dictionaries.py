'''
Consider two dictionaries as dict1 and dict2. Merge these dictionaries and show the merged one.

Example 1:
Input:
dict1 = {"a":1}
dict2 = {"b":2}
Output: {'a': 1, 'b': 2}

Example 2:
Input:
dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}
Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

'''

# Solution:

def mergeDictionary(dict1,dict2):
  dict1.update(dict2)
  return dict1
  
print(mergeDictionary(dict1,dict2))
