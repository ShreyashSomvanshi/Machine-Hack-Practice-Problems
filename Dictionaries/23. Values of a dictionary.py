'''
Consider a dictionary as dict1 consisting of the keys and corresponding values. Obtain all the dictionary values in the form of a list.

Example 1:
Input: dict1 = {"A": 1,"B": 2,"C": 3}
Output: dict_values([1, 2, 3])

Example 2:
Input: dict1 = {"team":"Real Madrid","captain":"Benzema","manager":"Carlo Ancelotti"}
Output: dict_values(['Real Madrid', 'Benzema', 'Carlo Ancelotti'])
'''

# Solution:
def DictValues(dict1):
  return dict1.values()
  
print(DictValues(dict1))
