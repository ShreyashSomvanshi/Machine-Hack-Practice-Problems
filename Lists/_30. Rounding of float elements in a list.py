'''
Consider a list as list1 of N-elements containing integers and floats. Now write a python program to round
all the float elements to the closest integers and print the updated list in ascending order.

Example 1:
Input: list1 =[1, 2.234, 4.765, 9.12, 3, 3.88,&amp;nbsp;8.45]
Output: [1, 2, 3, 4, 5, 8, 9]

Example 2:
Input: list1 = [11,2,3.34,22,7.56]
Output: [2, 3, 8, 11, 22]

Hints: Use the round() method to round off the float elements
'''

# Solution:

def conversion_of_float_to_int(list1):
  h = []
  for i in list1:
    if (type(i) == int) or (type(i) == float):
      k=round(i)
      h.append(k)
    else:
      pass
  return sorted(h)
  

