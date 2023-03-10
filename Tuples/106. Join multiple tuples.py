'''
Consider three tuples as tuple1, tuple2 and tuple3. Print all the elements of tuple1, tuple2 and tuple3 in a single tuple.

Example 1:
Input:
tuple1 = (1,2,3)
tuple2 = ("r9","m10","b23")
tuple3 = (17,23,9)
Output: (1, 2, 3, 'r9', 'm10', 'b23', 17, 23, 9)

Example 2:
Input:
tuple1 = ("ak17","sp17","na17")
tuple2 = ("machine","hack","aim")
tuple3 = ("shiv","ani")
Output: ('ak17', 'sp17', 'na17', 'machine', 'hack', 'aim', 'shiv', 'ani')

'''

# Solution:

def add(tuple1,tuple2,tuple3):
  return tuple1+tuple2+tuple3
  
print(add(tuple1,tuple2,tuple3))

