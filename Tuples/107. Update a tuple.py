'''
Consider a tuple as tuple1 made up of N elements. First, add an element X to the tuple at the end.
Second, replace the first element of the tuple with a new element Y. Finally print the finalized tuple.

Example 1:
Input:
tuple1 = ("Replace me with y", "fun", "done")
X = "Add me at end"
Y = "Replaced"
Output: ('Replaced', 'fun', 'done', 'Add me at end')

Example 2:
Input:
tuple1 = ("Don't replace me", "machine", "hack")
X = 17
Y = 17
Output: (17, 'machine', 'hack', 17)

'''

# Solution:
def updation_of_tuple(tuple1,X,Y):
  o=len(tuple1)
  g=list(tuple1)
  g.insert(o,X)
  g[0]=Y
  u=tuple(g)
  return u
  
print(updation_of_tuple(tuple1,X,Y))


