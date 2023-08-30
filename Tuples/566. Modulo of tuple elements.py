'''
Return the modulo of the elements of a given tuple x.

Example 1:
Input:
x = (10, 4, 5, 6)
y = (5, 6, 7, 5)
Output: (0, 4, 5, 1)

Example 2:
Input:
x = (10, 4, 5, 6,5,7,6,7,8,4,5)
y = (5, 6, 7, 5,5,7,6,3)
Output: (0, 4, 5, 1, 0, 0, 0, 1)
'''

# Soln:
def moduloTuple(x,y):
  t = []
  for i in range(len(y)):
    v = x[i]%y[i]
    t.append(v)
  return tuple(t)
  
print(moduloTuple(x,y))
