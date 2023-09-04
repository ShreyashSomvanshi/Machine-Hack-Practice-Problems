'''
Obtain all the items of a given dictionary dict1 in a list of tuples.

Example 1:
Input: dict1 = {"a":1,"b":2,"c":3,"d":4}
Output: dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

Example 2:
Input: dict1 = {"Tallest waterfall": "Angel Falls","Longest river": "Nile"}
Output: dict_items([('Tallest waterfall', 'Angel Falls'), ('Longest river', 'Nile')])
'''

# Soln:

## New: 25ms
def dictionaryItems(dict1):
  print(dict1.items())
  
dictionaryItems(dict1)


### 26ms
def dictionaryItems(dict1):
  return dict1.items()
  
print(dictionaryItems(dict1))
