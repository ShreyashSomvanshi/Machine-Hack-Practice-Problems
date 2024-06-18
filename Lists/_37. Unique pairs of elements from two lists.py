'''
Consider two lists list1 and list2 consisting of integer elements. Obtain all possible 
pairs of elements so that elements are not identical in pairs.

Example 1:
Input:
list1 = [1,2,3]
list2 = [5]
Output: [[1, 5], [2, 5], [3, 5]]

Example 2:
Input:
list1 = [1,2]
list2 = [3,4]
Output: [[1, 3], [1, 4], [2, 3], [2, 4]]
'''

# Soln1:

def combination(list1, list2):
    return [[i, j] for i in list1 for j in list2]

print(combination(list1, list2))


# Soln2:
def combination(list1,list2):
  p = []
  for i in list1:
    for j in list2:
      p.append([i, j])
  return p

print(combination(list1,list2))
