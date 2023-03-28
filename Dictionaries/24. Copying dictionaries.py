'''
Copy a given dictionary dict1 to a new dictionary dict2.

Example 1:
Input: dict1 = {"a":1,"b":2,"c":3,"d":4}
Output: {"a":1,"b":2,"c":3,"d":4}

Example 2:
Input: dict1 = {"wild":["tiger","lion"],"pet":["dog","cat"]}
Output: {'wild': ['tiger', 'lion'], 'pet': ['dog', 'cat']}

'''

# Solution:

def copyDictionary(dict1):
  dictt = dict1.copy() 
  return dictt
  
print(copyDictionary(dict1))

